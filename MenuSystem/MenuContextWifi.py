from MenuSystem.MenuContext import *


class MenuContextWifi(MenuContext):

    def __init__(self, inManager, inLcd):
        super(MenuContextWifi, self).__init__(inManager, inLcd)
        self.title = "Wifi Setup - " + self.manager.getIpAddress()     #Title to display at the top of the display when this menu is active.
        self.entries = ["Switch to AP","Choose Network", "Network Details"]           #Holds a reference to all the possible entries in the menu
        self.parent = "Settings"

    """
    Callback methods that perform an action for a button press based on which menu the user is in.
    Need to be implemented by child classes
    """
    def onSet(self):
        if self.currentEntry==0:
            pass
        elif self.currentEntry==1:
            pass
        elif self.currentEntry==2:
            self.title = "Wifi Setup - " + self.manager.getIPAddress()
            self.displayMessage("Updated")
            self.updateDisplay()

    def connectToNetwork(self):
        pass

