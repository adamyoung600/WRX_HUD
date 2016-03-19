

class HUDMainDummy():

    def __init__(self):
        pass

    def _loadConfig(self):
        pass

    def calculateGear(self, engineSpeed, vehicleSpeed):
        pass

    def setMonitoredParams(self, inParamIds):
        pass

    ##########################################
    # Keyboard input handling
    ##########################################
    def checkForKeyboardInput(self):
        pass

    def setMenuMode(self, enableMenuMode):
        self._menuMode = enableMenuMode

    def setActiveMonitorMode(self, inIsSet):
        self._inActiveMonitoredMode = inIsSet

