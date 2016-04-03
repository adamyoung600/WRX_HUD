from MenuSystem.MenuContextMain import MenuContextMain
from MenuSystem.MenuContextMonitoredParameter import MenuContextMonitoredParameter
from MenuSystem.MenuContextSetParameters import MenuContextSetParameters
from MenuSystem.MenuContextPassiveMode import MenuContextPassiveMode
from MenuSystem.MenuContextPeakBoost import *
from MenuSystem.MenuContextDtcCode import *
from MenuSystem.MenuContextSettings import *
from MenuSystem.MenuContextShiftLights import *
from MenuSystem.MenuContextSoftReset import *
from MenuSystem.MenuContextWifi import *
from MenuSystem.MenuContextNetworkDetails import *
from MenuSystem.MenuContextOpenNetworks import *

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
                Display Peak
                Reset Peak
            Trouble Codes
            Settings
                Shift Lights
                Wifi Setup
                    AP Mode
                    Find Open Network
                    Iphone Tether
                    Network Details
                Soft Reset
                Update
        """
        self.contexts['Main'] = MenuContextMain(self, inLcd)
        self.contexts['Monitored Params'] = MenuContextMonitoredParameter(self, inLcd)
        self.contexts['Set Parameters'] = MenuContextSetParameters(self, inLcd)
        self.contexts['Set Passive Mode'] = MenuContextPassiveMode(self, inLcd)
        self.contexts['Peak Boost'] = MenuContextPeakBoost(self, inLcd)
        self.contexts['Trouble Codes'] = MenuContextDtcCode(self, inLcd)
        self.contexts['Settings'] = MenuContextSettings(self, inLcd)
        self.contexts['Shift Lights'] = MenuContextShiftLights(self, inLcd)
        self.contexts['Wifi Setup'] = MenuContextWifi(self, inLcd)
        self.contexts['Find Open Network'] = MenuContextOpenNetworks(self, inLcd)
        self.contexts['Network Details'] = MenuContextNetworkDetails(self, inLcd)
        self.contexts['Soft Reset'] = MenuContextSoftReset(self, inLcd)

        self.currentContext = self.contexts['Main']
        self.menuMode = False
        self.monitoredParam1 = None
        self.monitoredParam2 = None

        #TODO init peak boost
        self.peakBoost = 0.0
        #TODO init shift light thresholds
        self.shiftLightThresholds = [3000, 4000, 5000, 6000]


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

    def calibrateBoost(self):
        self.main.calibrateBoost()

    def setPeakBoost(self, inBoost):
        self.peakBoost = inBoost

    def getPeakBoost(self):
        return self.peakBoost

    def setShiftLightThreshold(self, inThresholdNum, inValue):
        self.shiftLightThresholds[inThresholdNum] = inValue

    def getShiftLightThreshold(self, inThresholdNum):
        if inThresholdNum >= 0 and inThresholdNum < 4:
            return self.shiftLightThresholds[inThresholdNum]

    def resetSystem(self):
        self.main.resetSystem()

    def getIpAddress(self):
        return self.main.getIpAddress('wlan0')

    def getSSID(self):
        return self.main.getSSID()

    def getOpenNetworks(self):
        return self.main.getOpenNetworks()

    def connectToNetwork(self, inSSID):
        return(self.main.connectToNetwork(inSSID))



