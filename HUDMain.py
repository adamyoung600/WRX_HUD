

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
        self._logFile.info('SWC Start')
        self._keyboard = Keyboard()
        self._logFile.info('SWC Done')
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
            self.checkForKeyboardInput()



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
        if inputVal != None:
            self._boostGauge.calibrate()



