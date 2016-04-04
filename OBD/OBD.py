###########################################################################
#
# The below functionality was take from a project called pyobd.  Git Hub:
# https://github.com/peterh/pyobd
# I only needed the trouble code logic so I removed the rest.
#
# Copyright 2004 Donour Sizemore (donour@uchicago.edu)
# Copyright 2009 Secons Ltd. (www.obdtester.com)
#
# This file is part of pyOBD.
#
# pyOBD is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# pyOBD is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyOBD; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
###########################################################################

import serial
import string
import time
from math import ceil

GET_DTC_COMMAND = "03"
CLEAR_DTC_COMMAND = "04"
GET_FREEZE_DTC_COMMAND = "07"

# __________________________________________________________________________
def hex_to_int(str):
    i = eval("0x" + str, {}, {})
    return i


def decrypt_dtc_code(code):
    """Returns the 5-digit DTC code from hex encoding"""
    dtc = []
    current = code
    for i in range(0, 3):
        if len(current) < 4:
            raise "Tried to decode bad DTC: %s" % code

        tc = hex_to_int(current[0])  # typecode
        tc = tc >> 2
        if tc == 0:
            type = "P"
        elif tc == 1:
            type = "C"
        elif tc == 2:
            type = "B"
        elif tc == 3:
            type = "U"
        else:
            raise tc

        dig1 = str(hex_to_int(current[0]) & 3)
        dig2 = str(hex_to_int(current[1]))
        dig3 = str(hex_to_int(current[2]))
        dig4 = str(hex_to_int(current[3]))
        dtc.append(type + dig1 + dig2 + dig3 + dig4)
        current = current[4:]
    return dtc


# __________________________________________________________________________

class OBDPort:
    """ OBDPort abstracts all communication with OBD-II device."""

    def __init__(self):
        """Initializes port by resetting device and gettings supported PIDs. """
        self.ELMver = "Unknown"
        self.State = 1  # state SERIAL is 1 connected, 0 disconnected (connection failed)

        print("Opening interface (serial port)")

        try:
            self.port = serial.Serial(
                port='/dev/ttyUSB0',
                baudrate=9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=2000, )

        except serial.SerialException as e:
            print e
            self.State = 0
            return None

        print("Interface successfully " + self.port.portstr + " opened")
        print("Connecting to ECU...")

        try:
            self.send_command("atz")  # initialize
        except serial.SerialException:
            self.State = 0
            return None

        self.ELMver = self.get_result()
        self.send_command("ate0")  # echo off
        self.send_command("0100")
        ready = self.get_result()
        print("0100 response:" + ready)
        return None


    def close(self):
        """ Resets device and closes all associated filehandles"""

        if (self.port != None) and self.State == 1:
            self.send_command("atz")
            self.port.close()

        self.port = None
        self.ELMver = "Unknown"

    def send_command(self, cmd):
        """Internal use only: not a public interface"""
        if self.port:
            self.port.flushOutput()
            self.port.flushInput()
            for c in cmd:
                self.port.write(c)
            self.port.write("\r\n")


    def get_result(self):
        """Internal use only: not a public interface"""
        time.sleep(0.1)
        if self.port:
            buffer = ""
            while 1:
                c = self.port.read(1)
                if c == '\r' and len(buffer) > 0:
                    break
                else:
                    if buffer != "" or c != ">":  # if something is in buffer, add everything
                        buffer = buffer + c

            return buffer
        return None


        #
        # fixme: j1979 specifies that the program should poll until the number
        # of returned DTCs matches the number indicated by a call to PID 01
        #


    def get_dtc(self):
        """Returns a list of all pending DTC codes. Each element consists of
        a 2-tuple: (DTC code (string), Code description (string) )"""
        dtcLetters = ["P", "C", "B", "U"]
        r = self.queryDTC()
        dtcNumber = r[0]
        mil = r[1]
        DTCCodes = []

        print "Number of stored DTC:" + str(dtcNumber) + " MIL: " + str(mil)
        # get all DTC, 3 per mesg response
        for i in range(0, ((dtcNumber + 2) / 3)):
            self.send_command(GET_DTC_COMMAND)
            res = self.get_result()
            print "DTC result:" + res
            for i in range(0, 3):
                val1 = hex_to_int(res[3 + i * 6:5 + i * 6])
                val2 = hex_to_int(res[6 + i * 6:8 + i * 6])  # get DTC codes from response (3 DTC each 2 bytes)
                val = (val1 << 8) + val2  # DTC val as int

                if val == 0:  # skip fill of last packet
                    break

                DTCStr = dtcLetters[(val & 0xC000) > 14] + str((val & 0x3000) >> 12) + str((val & 0x0f00) >> 8) + str(
                    (val & 0x00f0) >> 4) + str(val & 0x000f)

                DTCCodes.append(["Active", DTCStr])

        # read mode 7
        self.send_command(GET_FREEZE_DTC_COMMAND)
        res = self.get_result()

        if res[:7] == "NO DATA":  # no freeze frame
            return DTCCodes

        print "DTC freeze result:" + res
        for i in range(0, 3):
            val1 = hex_to_int(res[3 + i * 6:5 + i * 6])
            val2 = hex_to_int(res[6 + i * 6:8 + i * 6])  # get DTC codes from response (3 DTC each 2 bytes)
            val = (val1 << 8) + val2  # DTC val as int

            if val == 0:  # skip fill of last packet
                break

            DTCStr = dtcLetters[(val & 0xC000) > 14] + str((val & 0x3000) >> 12) + str((val & 0x0f00) >> 8) + str(
                (val & 0x00f0) >> 4) + str(val & 0x000f)
            DTCCodes.append(["Passive", DTCStr])

        return DTCCodes


    def clear_dtc(self):
        """Clears all DTCs and freeze frame data"""
        self.send_command(CLEAR_DTC_COMMAND)
        r = self.get_result()
        return r


    def queryDTC(self):
        self.send_command("0101")  # 0101 is for DTC codes.  Statically set here.
        data = self.get_result()
        if data:
            data = self.interpret_result(data)
            if data != "NODATA":
                data = self.dtc_decrypt(data)
        else:
            return "NORESPONSE"
        return data


    def dtc_decrypt(code):
        # first byte is byte after PID and without spaces
        num = hex_to_int(code[:2])  # A byte
        res = []

        if num & 0x80:  # is mil light on
            mil = 1
        else:
            mil = 0

        # bit 0-6 are the number of dtc's.
        num = num & 0x7f

        res.append(num)
        res.append(mil)

        numB = hex_to_int(code[2:4])  # B byte

        for i in range(0, 3):
            res.append(((numB >> i) & 0x01) + ((numB >> (3 + i)) & 0x02))

        numC = hex_to_int(code[4:6])  # C byte
        numD = hex_to_int(code[6:8])  # D byte

        for i in range(0, 7):
            res.append(((numC >> i) & 0x01) + (((numD >> i) & 0x01) << 1))

        res.append(((numD >> 7) & 0x01))  # EGR SystemC7  bit of different
        return res
