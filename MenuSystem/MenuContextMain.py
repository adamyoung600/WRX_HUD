import Hardware.SH1106.SH1106LCD
from MenuSystem.MenuContext import *


class MenuContextMain(MenuContext):

    def __init__(self, inManager, inLcd):
        super(MenuContextMain, self).__init__(inManager, inLcd)
        self.title = "Main"         #Title to display at the top of the display when this menu is active.
        self.entries = ["Monitored Parameters", "Peak Boost", "Trouble Codes", "Settings"]           #Holds a reference to all the possible entries in the menu

    """
    Callback methods that perform an action for a button press based on which menu the user is in.
    """
    def onBack(self):
        #Exit menuingMode
        self.manager.menuMode = False
