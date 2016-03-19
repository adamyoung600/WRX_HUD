import Hardware.SH1106.SH1106LCD
from MenuSystem.MenuContext import *


class MenuContextPassiveMode(MenuContext):

    def __init__(self, inManager, inLcd):
        super(MenuContextPassiveMode,self).__init__(inManager, inLcd)
        self.title = "Set Passive Mode"     #Title to display at the top of the display when this menu is active.
        self.entries = ["Yes", "No"]           #Holds a reference to all the possible entries in the menu
        self.parent = "Monitored Params"


    """
    Used to display the menu data on the LCD
    """

    """
    Callback methods that perform an action for a button press based on which menu the user is in.
    """
    def onSet(self):
        if self.currentEntry == 0:
            self.manager.setActiveMonitorMode(True)
            self.displayMessage("Set Active")

        elif self.currentEntry == 1:
            self.manager.setActiveMonitorMode(False)
            self.displayMessage("Set Passive")





