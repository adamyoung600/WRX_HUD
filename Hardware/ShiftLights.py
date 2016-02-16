import RPi.GPIO as GPIO

class ShiftLights():

    def __init__(self, thresholds):
        self._greenLed = 27
        self._orangeLed = 22
        self._redLed = 23
        self._blueLed = 24
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._greenLed, GPIO.OUT)
        GPIO.setup(self._orangeLed, GPIO.OUT)
        GPIO.setup(self._redLed, GPIO.OUT)
        GPIO.setup(self._blueLed, GPIO.OUT)
        self._anyLightsOn = False
        self._clearLights()
        self.setThresholds(thresholds)



    def setThresholds(self, thresholds):
        self._greenThreshold = thresholds[0]
        self._redThreshold = thresholds[1]
        self._orangeThreshold = thresholds[2]
        self._blueThreshold = thresholds[3]

    def _clearLights(self):
        GPIO.output(self._greenLed, False)
        GPIO.output(self._orangeLed, False)
        GPIO.output(self._redLed, False)
        GPIO.output(self._blueLed, False)
        self._anyLightsOn = False

    def update(self, rpm):
        if rpm < self._greenThreshold and not self._anyLightsOn:
            return
        elif rpm < self._greenThreshold and self._anyLightsOn:
            self._clearLights()
            return

        if rpm > self._greenThreshold:
            GPIO.output(self._greenLed, True)
        else:
            GPIO.output(self._greenLed, False)

        if rpm > self._orangeThreshold:
            GPIO.output(self._orangeLed, True)
        else:
            GPIO.output(self._orangeLed, False)

        if rpm > self._redThreshold:
            GPIO.output(self._redLed, True)
        else:
            GPIO.output(self._redLed, False)

        if rpm > self._blueThreshold:
            GPIO.output(self._blueLed, True)
        else:
            GPIO.output(self._blueLed, False)
