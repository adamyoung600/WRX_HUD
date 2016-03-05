import Hardware.SH1106.SH1106LCD
from MenuSystem.MenuContext import *


class MenuContextMenu(MenuContext):

    def __init__(self, inManager, inLcd):
        super(MenuContextMenu, self).__init__(inManager, inLcd)
        self.title = "Main"         #Title to display at the top of the display when this menu is active.
        self.entries = ["SSM Parameters", "Peak Boost", "Trouble Codes", "Settings"]           #Holds a reference to all the possible entries in the menu

    """
    Callback methods that perform an action for a button press based on which menu the user is in.
    """

    def onSet(self):
        if self.currentEntry==0:
            self.manager.setCurrentContext("Monitored Parameters")
        elif self.currentEntry==1:
            self.manager.setCurrentContext("Peak Boost")
        elif self.currentEntry==2:
            self.manager.setCurrentContext("Trouble Codes")
        elif self.currentEntry==3:
            self.manager.setCurrentContext("Wifi Config")

    def onBack(self):
        #Exit menuingMode
        self.manager.menuMode = False
