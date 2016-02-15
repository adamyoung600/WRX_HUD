# from Sh1106.GearIndicatorLCD import *
# from I2CConfig import *
# from WideHKOLED.WideHKOLED import *

import traceback
import time

from EngineData.SSM.pimonitor.PMConnection import PMConnection
from EngineData.SSM.pimonitor.PMXmlParser import PMXmlParser
from GearIndicator import GearIndicator
from Hardware.Input.Keyboard import Keyboard
from MenuSystem.MenuManager import MenuManager
from Util.Config import Config
from EngineData.EcuData import EcuData
from DataDisplay import DataDisplay
from Hardware.Input.SwitchPanel import SwitchPanel
from Hardware.ShiftLights import ShiftLights


class HUDMain():

    def __init__(self):

        self._keyboard = Keyboard()
        self._menuManager = MenuManager()
        self._gearIndicator = GearIndicator()
        self._dataDisplay = DataDisplay()

        self._ecu = EcuData()
        self._switchPanel = SwitchPanel()

        self._menuMode = False

        # Read in config from the file system.
        self._monitoredParamIDs = None
        self._rpmThresholds == None
        self._loadConfig()      # Sets the monitored params in the ecu as well.
        self._shiftLights = ShiftLights(self._rpmThresholds)

        self._oldGear = None
        self._newGear = None


    def mainLoop(self):
        while True:
            if not self._inMenuMode:
                # Query monitored parameters and update data display
                monitoredValues = self._ecu.getMonitoredParams()
                self._dataDisplay.update(monitoredValues)

                # UPdate Shift Lights
                rpm = int(self._ecu.getEngineSpeed())
                if self._switchPanel.isShiftLightEnabled():
                    self._shiftLights.update(rpm)

                # Update Gear Display
                if self._switchPanel.isLCDEnabled():
                    if not self._ecu.isInGear():
                        self._newGear = "N"
                    else:
                        self._newGear = self._ecu.getCurrentGear()

                    if self._newGear != self._oldGear:
                        self._oldGear = self._newGear
                        if self._newGear == "N":
                            self._gearIndicator.DisplayNeutral()
                        else:
                            self._gearIndicator.DisplayGear(self._newGear)

                #if self._ecu.getThrottlePedalAngle() > self._throttlePositionThreshold:
                    #Start Logging

                # Check for keyboard input
                self.checkForKeyboardInput()

            else:
                while self.menuMode:
                    self.checkForKeyboardInput()

    def _loadConfig(self):
        if self._config == None:
            self._config = Config()
        self._monitoredParamIDs = self._config.getMonitoredParams()
        self._rpmThresholds = self._config.getRpmThresholds()
        self._ecu.setMonitoredParams(self._monitoredParamIDs)


    def calculateGear(self, engineSpeed, vehicleSpeed):
        pass

    ##########################################
    # Keyboard input handling
    ##########################################
    def checkForKeyboardInput(self):
        inputVal = self._keyboard.getChar()

        if self._menuMode == False and inputVal != None:
            self.menuMode = True
            self._menuManager.enterMenuMode()
            return

        if inputVal == 'w':
            self.upButtonCallback()
        elif inputVal == 's':
            self.downButtonCallback()
        elif inputVal == 'p':
            self.setButtonCallback()
        elif inputVal == 'o':
            self.backButtonCallback()

    def setMenuMode(self, enableMenuMode):
        self._menuMode = enableMenuMode

    def upButtonCallback(self):
        self._menuManager.upButtonCallback()

    def downButtonCallback(self):
        self._menuManager.downButtonCallback()

    def setButtonCallback(self):
        self._menuManager.setButtonCallback()

    def backButtonCallback(self):
        self._menuManager.backButtonCallback()

