from MenuSystem.MenuContext import *


class MenuContextWifi(MenuContext):

    def __init__(self, inManager, inLcd):
        super(MenuContextWifi, self).__init__(inManager, inLcd)
        self.title = "Wifi Setup"     #Title to display at the top of the display when this menu is active.
        self.entries = ["Switch to AP","Choose Network", "Display IP"]           #Holds a reference to all the possible entries in the menu


    """
    Callback methods that perform an action for a button press based on which menu the user is in.
    Need to be implemented by child classes
    """
    def onUp(self):
        if self.currentEntry > 0:
            self.lastEntry = self.currentEntry
            self.currentEntry -= 1
            self.updateDisplay()

    def onDown(self):
        if self.currentEntry < len(self.entries)-1:
            self.lastEntry = self.currentEntry
            self.currentEntry += 1
            self.updateDisplay()

    def onSet(self):
        if self.currentEntry==0:
            pass
        elif self.currentEntry==1:
            pass

    def onBack(self):
        self.manager.setCurrentContext("Main Menu")

    def connectToNetwork(self):
        pass

