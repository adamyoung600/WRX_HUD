from MenuSystem.MenuContextMain import *
from MenuSystem.MenuContextMonitoredParameter import *
from MenuSystem.MenuContextPeakBoost import *
from MenuSystem.MenuContextDtcCode import *
from MenuSystem.MenuContextWifi import *

class MenuManager():

    def __init__(self, inLcd):
        self.lcd = inLcd
        #Spawn the menu contexts
        self.contexts = {}
        self.contexts['Main Menu'] = MenuContextMenu(self, inLcd)
        self.contexts['Monitored Parameters'] = MenuContextMonitoredParameter(self, inLcd)
        self.contexts['Peak Boost'] = MenuContextPeakBoost(self, inLcd)
        self.contexts['Trouble Codes'] = MenuContextDtcCode(self, inLcd)
        self.contexts['Wifi Config'] = MenuContextWifi(self, inLcd)

        self.currentContext = 'Main Menu'
        self.menuMode = False

    """
    Callbacks for buttons
    """
    def upButtonCallback(self):
        if self.menuMode:
            self.contexts[self.currentContext].onUp()

    def downButtonCallback(self):
        if self.menuMode:
            self.contexts[self.currentContext].onDown()

    def setButtonCallback(self):
        if self.menuMode:
            self.contexts[self.currentContext].onSet()
        else:
            self.menuMode = True
            self.currentContext = 'Main Menu'
            self.initiateDisplay()

    def backButtonCallback(self):
        if self.menuMode:
            self.contexts[self.currentContext].onBack()

    """
    Misc
    """
    def setCurrentContext(self, inContext):
        self.currentContext = inContext
        self.initiateDisplay()

    def initiateDisplay(self):
        self.contexts[self.currentContext].initDisplay()

    def enterMenuMode(self):
        self.menuMode = True
        self.initiateDisplay()

    def exitMenuMode(self):
        self.menuMode = False
        self.main.setMenuMode(False)