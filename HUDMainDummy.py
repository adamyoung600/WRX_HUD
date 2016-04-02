

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

    def setPassiveMonitorMode(self, inIsSet):
        self._inPassiveMonitoredMode = inIsSet

    def calibrateBoost(self):
        pass

    def resetSystem(self):
        print("Reset Called")