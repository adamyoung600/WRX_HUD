import RPi.GPIO as GPIO
import time

class BoostGauge():

    def __init__(self):
        self._calibratePin = 25
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._calibratePin, GPIO.OUT)
        GPIO.output(self._calibratePin, False)

    def calibrate(self):
        GPIO.output(self._calibratePin, True)
        time.sleep(0.25)
        GPIO.output(self._calibratePin, False)