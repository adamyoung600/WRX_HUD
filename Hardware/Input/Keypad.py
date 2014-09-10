import RPi.GPIO as GPIO
import time


class Keypad():

    def __init__(self, inMenuSystem):
        self.menuSystem = inMenuSystem
        self.debounceTimestamp = time.time()

        #Static mapping for keypad buttons to raspberry pi GPIO pins
        upPin = 25
        downPin = 24
        backPin = 22
        setPin = 23

        #Enable GPIO pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(upPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(downPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(backPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(setPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        #Set up GPIO interrupt callbacks
        GPIO.add_event_detect(upPin, GPIO.FALLING, callback=self.upButtonCallback)
        GPIO.add_event_detect(downPin, GPIO.FALLING, callback=self.downButtonCallback)
        GPIO.add_event_detect(backPin, GPIO.FALLING, callback=self.backButtonCallback)
        GPIO.add_event_detect(setPin, GPIO.FALLING, callback=self.setButtonCallback)

    def upButtonCallback(self, channel):
        tempTime = time.time()
        if(tempTime - self.debounceTimestamp) >= 0.3:
            self.menuSystem.upButtonCallback()
        self.debounceTimestamp = tempTime

    def downButtonCallback(self, channel):
        tempTime = time.time()
        if(tempTime - self.debounceTimestamp) >= 0.3:
            self.menuSystem.downButtonCallback()
        self.debounceTimestamp = tempTime

    def backButtonCallback(self, channel):
        tempTime = time.time()
        if(tempTime - self.debounceTimestamp) >= 0.3:
            self.menuSystem.backButtonCallback()
        self.debounceTimestamp = tempTime

    def setButtonCallback(self, channel):
        tempTime = time.time()
        if(tempTime - self.debounceTimestamp) >= 0.3:
            self.menuSystem.setButtonCallback()
        self.debounceTimestamp = tempTime