import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


upTimeStamp = 0
downTimeStamp = 0
backTimeStamp = 0
setTimeStamp = 0

def upCallback(channel):
    global upTimeStamp
    tempTime = time.time()
    if (tempTime - upTimeStamp) >= 0.2:
        print("Up")
        upTimeStamp = tempTime

def downCallback(channel):
    global downTimeStamp
    tempTime = time.time()
    if (tempTime - downTimeStamp) >= 0.2:
        print("Down")
        downTimeStamp = tempTime

def setCallback(channel):
    global setTimeStamp
    tempTime = time.time()
    if (tempTime - setTimeStamp) >= 0.2:
        print("Set")
        setTimeStamp = tempTime

def backCallback(channel):
    global backTimeStamp
    tempTime = time.time()
    if (tempTime - backTimeStamp) >= 0.2:
        print("Back")
        backTimeStamp = tempTime

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