from MenuSystem.MenuContext import *


class MenuContextSoftReset(MenuContext):

    def __init__(self, inManager, inLcd):
        super(MenuContextSoftReset,self).__init__(inManager, inLcd)
        self.title = "Confirm Shutdown"     #Title to display at the top of the display when this menu is active.
        self.entries = ["Yes", "No"]           #Holds a reference to all the possible entries in the menu
        self.parent = "Settings"

    """
    Callback methods that perform an action for a button press based on which menu the user is in.
    """
    def onSet(self):
        if self.currentEntry == 0:
            self.manager.resetSystem()
            self.displayMessage("Resetting...")

        elif self.currentEntry == 1:
            self.manager.setCurrentContext(self.parent)

    #Overide
    def displayMessage(self, inString):
        self.lcd.clearScreen()
        self.lcd.centerString(inString, 3)

