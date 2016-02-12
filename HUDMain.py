# from Sh1106.GearIndicatorLCD import *
# from I2CConfig import *
# from WideHKOLED.WideHKOLED import *

import traceback
import time

from EngineData.SSM.pimonitor.PMConnection import PMConnection
from EngineData.SSM.pimonitor.PMXmlParser import PMXmlParser
from Hardware.Input.Keyboard import Keyboard
from MenuSystem.MenuManager import MenuManager


class HUDMain():

    def __init__(self):

        self._keyboard = Keyboard()
        self._menuManager = MenuManager()
        self._menuMode = False

    def mainLoop(self):
        pass

    ##########################################
    #Keyboard input handling
    ##########################################
    def checkForKeyboardInput(self):
        input_val = self._keyboard.getChar()

        if self._menuMode == False and input_val != None:
            self.menuMode = True
            return

        if input_val == 'w':
            self.upButtonCallback()
        elif input_val == 's':
            self.downButtonCallback()
        elif input_val == 'p':
            self.setButtonCallback()
        elif input_val == 'o':
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

