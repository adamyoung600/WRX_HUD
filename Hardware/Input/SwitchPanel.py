import RPi.GPIO as GPIO

class SwitchPanel():

    def __init__(self):
        #TODO: fill in the correct pins
        self._shiftLightPin = 23
        self._lcdPin = 24
        self._bounctTime = 300

        #Shift Lights Setup
        GPIO.setup(self._shiftLightPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self._shiftLightPin, GPIO.RISING, callback=setShift, bouncetime=self._bounctTime)
        GPIO.add_event_detect(self._shiftLightPin, GPIO.FALLING, callback=unsetShift, bouncetime=self._bounctTime)
        self._shiftLightsEnabled = False
        if GPIO.input(self._shiftLightPin):
            self._shiftLightsEnabled = True

        #LCD Enable Setup
        GPIO.setup(self._lcdPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self._lcdPin, GPIO.RISING, callback=setLcd, bouncetime=self._bounctTime)
        GPIO.add_event_detect(self._lcdPin, GPIO.FALLING, callback=unsetLcd, bouncetime=self._bounctTime)
        self._lcdEnabled = False
        if GPIO.input(self._shiftLightPin):
            self._lcdEnabled = True

    def setShift(self):
        self._shiftLightsEnabled = True

    def unsetShift(self):
        self._shiftLightsEnabled = False

    def setLcd(self):
        self._lcdEnabled = True

    def unsetLcd(self):
        self._lcdEnabled = False

    def isShiftLightEnabled(self):
        return self._shiftLightsEnabled

    def isLCDEnabled(self):
        return self._lcdEnabled
