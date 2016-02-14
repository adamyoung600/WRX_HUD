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


class HUDMain():

    def __init__(self):

        self._keyboard = Keyboard()
        self._menuManager = MenuManager()
        self._gearIndicator = GearIndicator()


        self._menuMode = False

        # Read in config from the file system.
        self.__monitoredParamIDs = None
        self.__rpmThresholds == None
        self._loadConfig()




    def mainLoop(self):
        pass
        # Query monitored parameters and update data display


    def _loadConfig(self):
        if self.__config == None:
            self.__config = Config()
        self.__monitoredParamIDs = self.__config.getMonitoredParams()
        self.__rpmThresholds = self.__config.getRpmThresholds()

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

