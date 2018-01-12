

import traceback
import time
import os
import socket
import fcntl
import struct
import RPi.GPIO as GPIO
from subprocess import check_output

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
from Hardware.BoostGauge import BoostGauge
from Util.LogFile import LogFile


class HUDMain():

    def __init__(self):
        #Logging
        self._logFile = LogFile()
        self._logFile.info('=== Start System Initialization ===')

        #Rasp pi specific
        GPIO.setmode(GPIO.BCM)

        #INPUTS
        self._logFile.info('ECU Start')
        self._ecu = EcuData()
        self._logFile.info('ECU Done')
        self._logFile.info('Switch Panel Start')
        self._switchPanel = SwitchPanel()
        self._logFile.info('Switch Panel Done')

        #OUTPUTS
        self._logFile.info('Gear Display Start')
        self._gearIndicator = GearIndicator()
        self._logFile.info('Gear Display Done')
        self._logFile.info('Boost Gauge Start')
        self._boostGauge = BoostGauge()
        self._logFile.info('Boost Gauge Done')

        self._menuMode = False

        # Read in config from the file system.
        self._monitoredParamIDs = None
        self._rpmThresholds == None
        self._inActiveMonitoredMode = False
        self._logFile.info('Read Config Start')
        self._loadConfig()      # Sets the monitored params in the ecu as well.
        self._logFile.info('Read Config Done')
        self._logFile.info('Shift Lights Start')
        self._shiftLights = ShiftLights(self._rpmThresholds)
        self._logFile.info('Shift Lights Done')

        self._oldGear = None
        self._newGear = None

        self._logFile.info('=== System Initialization Complete ===')

    def mainLoop(self):
        while True:
            # Have the ECU update all of the parameters it needs on this loop
            self._ecu.refreshData()

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



    def _loadConfig(self):
        if not self._config:
            self._config = Config()
        self._monitoredParamIDs = self._config.getMonitoredParams()
        self._rpmThresholds = self._config.getRpmThresholds()
        self._ecu.setMonitoredParams(self._monitoredParamIDs)

    def calculateGear(self, engineSpeed, vehicleSpeed):
        pass

    def setMonitoredParams(self, inParamIds):
        self._monitoredParamIDs = inParamIds
        self._ecu.setMonitoredParams(self._monitoredParamIDs)

    ##########################################
    # Keyboard input handling
    ##########################################
    def checkForKeyboardInput(self):
        inputVal = self._keyboard.getChar()

        if self._menuMode == False and inputVal != None:
            self.menuMode = True
            self._menuManager.enterMenuMode()
            return

        #Key assignment here is pretty arbitrary
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

    def setPassiveMonitorMode(self, inIsSet):
        self._inPassiveMonitoredMode = inIsSet


#TODO: Below check if in passive mode first before passing button callbacks to menu manager
    def upButtonCallback(self):
        self._menuManager.upButtonCallback()

    def downButtonCallback(self):
        self._menuManager.downButtonCallback()

    def setButtonCallback(self):
        self._menuManager.setButtonCallback()

    def backButtonCallback(self):
        self._menuManager.backButtonCallback()

    def calibrateBoost(self):
        self._boostGauge.calibrate()

    def resetSystem(self):
        os.system("sudo reboot")

    def shutdownSystem(self):
        os.system("sudo shutdown -h now")

# Below stolen from http://code.activestate.com/recipes/439094-get-the-ip-address-associated-with-a-network-inter/
    def getIpAddress(self, inInterface):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', inInterface[:15])
        )[20:24])

    def getSSID(self):
        output = check_output(["iwconfig", "wlan0"])
        ssid = "error"
        for line in output.split():
            if "ESSID" in line:
                ssid = line.split(':')[1].replace('\"','')
        return ssid

    """
    getOpenNetworks

    Parses the output of "iwlist wlan0 scan" to find all open wifi networks.

    Returns - List of SSIDs of all open networks in range
    """
    def getOpenNetworks(self):
        output = check_output(["iwlist", "wlan0", "scan"])
        networks = []
        ssid = None
        for line in output.split("\n"):
            if "ESSID" in line:
                ssid = line.split(':')[1].replace('\"','')
            if "Encryption key:off" in line:
                networks.append(ssid)
        return networks

    #Has to return a boolean
    def connectToNetwork(self, inSSID):
        print("Received request to connect to " + inSSID)
        return True