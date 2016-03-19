from MenuSystem.MenuContextMain import MenuContextMain
from MenuSystem.MenuContextMonitoredParameter import MenuContextMonitoredParameter
from MenuSystem.MenuContextSetParameters import MenuContextSetParameters
from MenuSystem.MenuContextPassiveMode import MenuContextPassiveMode
from MenuSystem.MenuContextPeakBoost import *
from MenuSystem.MenuContextDtcCode import *
from MenuSystem.MenuContextWifi import *

class MenuManager():

    def __init__(self, inLcd, inMain):
        self.lcd = inLcd
        self.main = inMain
        #Spawn the menu contexts
        self.contexts = {}
        """
        Main
            MonitoredParameters
                Set Parameters
                    Parameter List
                Set Passive Mode
            Peak Boost
            Trouble Codes
            Settings
        """
        self.contexts['Main'] = MenuContextMain(self, inLcd)
        self.contexts['Monitored Params'] = MenuContextMonitoredParameter(self, inLcd)
        self.contexts['Set Parameters'] = MenuContextSetParameters(self, inLcd)
        self.contexts['Set Passive Mode'] = MenuContextPassiveMode(self, inLcd)
        self.contexts['Peak Boost'] = MenuContextPeakBoost(self, inLcd)
        self.contexts['Trouble Codes'] = MenuContextDtcCode(self, inLcd)
        self.contexts['Settings'] = MenuContextWifi(self, inLcd)

        self.currentContext = self.contexts['Main']
        self.menuMode = False
        self.monitoredParam1 = None
        self.monitoredParam2 = None

    """
    Callbacks for buttons
    """
    def upButtonCallback(self):
        if self.menuMode:
            self.currentContext.onUp()

    def downButtonCallback(self):
        if self.menuMode:
            self.currentContext.onDown()

    def setButtonCallback(self):
        if self.menuMode:
            self.currentContext.onSet()
        else:
            self.menuMode = True
            self.currentContext = self.contexts['Main']
            self.initiateDisplay()

    def backButtonCallback(self):
        if self.menuMode:
            self.currentContext.onBack()

    """
    Misc
    """
    def setCurrentContext(self, inContext):
        self.currentContext = self.contexts[inContext]
        self.initiateDisplay()

    def setCurrentContextDirectly(self, inContext):
        self.currentContext = inContext
        self.initiateDisplay()

    def initiateDisplay(self):
        self.currentContext.initDisplay()

    def enterMenuMode(self):
        self.menuMode = True
        self.initiateDisplay()

    def exitMenuMode(self):
        self.menuMode = False
        self.main.setMenuMode(False)

    def setMonitoredParam(self, inParamID, inParamNum):
        if inParamNum == 1:
            self.monitoredParam2 = inParamID
        elif inParamNum == 2:
            self.monitoredParam1 = inParamID

    def setPassiveMonitorMode(self, inIsSet):
        self.main.setPassiveMonitorMode(inIsSet)

    def updateMonitoredParameters(self):
        self.main.setMonitoredParams([self.monitoredParam1, self.monitoredParam2])


