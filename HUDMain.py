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


class HUDMain():

    def __init__(self):

        self._keyboard = Keyboard()
        self._menuManager = MenuManager()
        self._gearIndicator = GearIndicator()
        self._dataDisplay = DataDisplay()
        self._ecu = EcuData()


        self._menuMode = False

        # Read in config from the file system.
        self._monitoredParamIDs = None
        self._rpmThresholds == None
        self._loadConfig()




    def mainLoop(self):
        pass
        # Query monitored parameters and update data display
        monitoredValues = self._ecu.getMonitoredParams()
        self._dataDisplay.update(monitoredValues)


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

