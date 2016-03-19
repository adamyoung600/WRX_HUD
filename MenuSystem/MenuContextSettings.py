import Hardware.SH1106.SH1106LCD
from MenuSystem.MenuContext import *


class MenuContextSettings(MenuContext):

    def __init__(self, inManager, inLcd):
        super(MenuContextSettings, self).__init__(inManager, inLcd)
        self.title = "Settings"         #Title to display at the top of the display when this menu is active.
        self.entries = ["Shift Lights","Logging Trigger","Calibrate Boost","Wifi Config","Soft Reset"]           #Holds a reference to all the possible entries in the menu


    """
    Callback methods that perform an action for a button press based on which menu the user is in.
    """

    def onSet(self):
        if self.currentEntry==0:
            pass
        elif self.currentEntry==1:
            pass
        elif self.currentEntry==2:
            pass
        elif self.currentEntry==3:
            pass

    def onBack(self):
        #Exit menuingMode
        self.manager.menuMode = False
