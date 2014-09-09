import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def upCallback(channel):
    print("Up")

def downCallback(channel):
    print("Down")

def setCallback(channel):
    print("Set")

def backCallback(channel):
    print("Back")

GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(22, GPIO.FALLING, callback=setCallback)
GPIO.add_event_detect(23, GPIO.FALLING, callback=backCallback)
GPIO.add_event_detect(24, GPIO.FALLING, callback=downCallback)
GPIO.add_event_detect(25, GPIO.FALLING, callback=upCallback)

i = 0
while True:
    print(i)
    i=i+1
    time.sleep(1)