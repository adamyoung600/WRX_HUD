#!/usr/bin/env python3
#
# W. Greathouse 13-Feb-2013
# S. Ludwig 26-Oct-2014
#
# Inspired by bcm2835 source - http://www.airspayce.com/mikem/bcm2835/
#
#   Enable I2C on P1 and P5 (Rev 2 boards only)
#

# #######
# For I2C configuration test
import os
import mmap
import time

BLOCK_SIZE = 4096
BCM2708_PERI_BASE = 0x20000000 # Base address of peripheral registers
GPIO_BASE = (BCM2708_PERI_BASE + 0x00200000)  # Address of GPIO registers
GPFSEL0 = 0x0000 # Function select 0
GPFSEL2 = 0x0008 # Function select 2
GPPUD = 0x0094 # GPIO Pin Pull-up/down Enable
GPPUDCLK0 = 0x0098 # GPIO Pin Pull-up/down Enable Clock 0
GPIO_PUD_OFF = 0b00   # Off - disable pull-up/down
GPIO_PUD_UP = 0b10    # Enable Pull Up control

def get_revision():
    with open('/proc/cpuinfo') as lines:
        for line in lines:
            if line.startswith('Revision'):
                return int(line.strip()[-4:],16)
    raise RuntimeError('No revision found.')

def i2cConfig():
    if get_revision() <= 3:
        print("Rev 2 or greater Raspberry Pi required.")
        return

    # Use /dev/mem to gain access to peripheral registers
    mf = os.open("/dev/mem", os.O_RDWR|os.O_SYNC)
    memory = mmap.mmap(mf, BLOCK_SIZE, mmap.MAP_SHARED,
                mmap.PROT_READ|mmap.PROT_WRITE, offset=GPIO_BASE)
    # can close the file after we have mmap
    os.close(mf)

    # each 32 bit register controls the functions of 10 pins, each 3 bit, starting at the LSB
    # 000 = input
    # 100 = alt function 0

    # Read function select registers
    # GPFSEL0 -- GPIO 0,1 I2C0   GPIO 2,3 I2C1
    memory.seek(GPFSEL0)
    reg0 = int.from_bytes(memory.read(4), byteorder='little')

    # GPFSEL0 bits --> x[20] SCL1[3] SDA1[3]
    #                        GPIO3   GPIO2   GPIO1   GPIO0
    reg0_mask = 0b00000000000000000000111111111111
    reg0_conf = 0b00000000000000000000100100000000
    if reg0 & reg0_mask != reg0_conf:
        print("register 0 configuration of I2C 1 not correct. Updating.")
        reg0 = (reg0 & ~reg0_mask) | reg0_conf
        memory.seek(GPFSEL0)
        memory.write(reg0.to_bytes(4, byteorder='little'))


    # GPFSEL2 -- GPIO 28,29 I2C0
    memory.seek(GPFSEL2)
    reg2 = int.from_bytes(memory.read(4), byteorder='little')

    # GPFSEL2 bits --> x[2] SCL0[3] SDA0[3] x[24]
    #                       GPIO29  GPIO28
    reg2_mask = 0b00111111000000000000000000000000
    reg2_conf = 0b00100100000000000000000000000000
    if reg2 & reg2_mask != reg2_conf:
        print("register 2 configuration of I2C 0 not correct. Updating.")
        reg2 = (reg2 & ~reg2_mask) | reg2_conf
        memory.seek(GPFSEL2)
        memory.write(reg2.to_bytes(4, byteorder="little"))

    # Configure pull up resistors for GPIO28 and GPIO29
    def configure_pull_up(pin):
        memory.seek(GPPUD)
        memory.write(GPIO_PUD_UP.to_bytes(4, byteorder="little"))
        time.sleep(10e-6)

        memory.seek(GPPUDCLK0)
        memory.write((1 << pin).to_bytes(4, byteorder="little"))
        time.sleep(10e-6)

        memory.seek(GPPUD)
        memory.write(GPIO_PUD_OFF.to_bytes(4, byteorder="little"))

        memory.seek(GPPUDCLK0)
        memory.write((0 << pin).to_bytes(4, byteorder="little"))

    configure_pull_up(28)
    configure_pull_up(29)

    # No longer need the mmap
    memory.close()


if __name__ == '__main__':
    i2cConfig()