from MenuSystem.MenuContext import *

class MenuContextOpenNetworks(MenuContext):

    def __init__(self, inManager, inLcd):
        super(MenuContextOpenNetworks, self).__init__(inManager, inLcd)
        self.title = "Open Networks"     #Title to display at the top of the display when this menu is active.
        self.entries = self.manager.getOpenNetworks()           #Holds a reference to all the possible entries in the menu
        if len(self.entries) > 6:
            self.entries = self.entries[0:7]
        self.parent = "Wifi Setup"

    """
    Callback methods that perform an action for a button press based on which menu the user is in.
    Need to be implemented by child classes
    """
    def onSet(self):
        self.displayMessage("Connecting...")
        connectSuccessful = self.manager.connectToNetwork(self.currentEntry)
        if connectSuccessful:
            self.displayMessage("ConnectSuccessful")
        else:
            self.displayMessage("ConnectFailed")
        time.sleep(1)
        self.initDisplay()

    #Overide
    def displayMessage(self, inString):
        self.lcd.clearScreen()
        self.lcd.centerString(inString, 3)

