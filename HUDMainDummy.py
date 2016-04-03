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