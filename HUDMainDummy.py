import socket
import fcntl
import struct
from subprocess import check_output

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

    def setPassiveMonitorMode(self, inIsSet):
        self._inPassiveMonitoredMode = inIsSet

    def calibrateBoost(self):
        pass

    def resetSystem(self):
        print("Reset Called")

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
