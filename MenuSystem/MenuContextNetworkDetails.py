from MenuSystem.MenuContext import *


class MenuContextNetworkDetails(MenuContext):

    def __init__(self, inManager, inLcd):
        super(MenuContextNetworkDetails, self).__init__(inManager, inLcd)
        self.title = "NetworkDetails"     #Title to display at the top of the display when this menu is active.
        self.parent = "Wifi Setup"

    """
    Callback methods that perform an action for a button press based on which menu the user is in.
    Need to be implemented by child classes
    """
    def initDisplay(self):
        self.lcd.clearScreen()
        #Display title
        self.lcd.displayString(self.title, 0, 0)
        self.lcd.displayString("---------------------", 1, 0)
        #Display network details
        self.lcd.displayString("SSID: "+ self.manager.getSSID(), 2, 5)
        self.lcd.displayString("IP: "+ self.manager.getIpAddress(), 3, 5)

    #Make all buttons just go back up a level
    def onUp(self):
        self.onBack()
    def onDown(self):
        self.onBack()
    def onSet(self):
        self.onBack()

