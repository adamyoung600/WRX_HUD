# from Sh1106.GearIndicatorLCD import *
# from I2CConfig import *
# from WideHKOLED.WideHKOLED import *

import traceback
import time

#from EngineData.SSM.pimonitor.PMConnection import PMConnection
#from EngineData.SSM.pimonitor.PMXmlParser import PMXmlParser
from GearIndicator import GearIndicator
from Hardware.Input.Keyboard import Keyboard
from MenuSystem.MenuManager import MenuManager
from Util.Config import Config
from EngineData.EcuData import EcuData
from DataDisplay import DataDisplay
from Hardware.Input.SwitchPanel import SwitchPanel
from Hardware.ShiftLights import ShiftLights


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

