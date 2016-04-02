from MenuSystem.MenuContext import *


class MenuContextSettings(MenuContext):

    def __init__(self, inManager, inLcd):
        super(MenuContextSettings, self).__init__(inManager, inLcd)
        self.title = "Settings"         #Title to display at the top of the display when this menu is active.
        self.entries = ["Shift Lights","Logging Trigger","Calibrate Boost","Wifi Setup","Soft Reset"]           #Holds a reference to all the possible entries in the menu


    """
    Callback methods that perform an action for a button press based on which menu the user is in.
    """

    def onSet(self):
        if self.currentEntry==1:     #Logging Trigger
            pass
        elif self.currentEntry==2:  #Calibrate Booste
            self.manager.calibrateBoost()
            self.displayMessage("Calibration Done")
        else:
            if len(self.entries) > self.currentEntry:
                self.manager.setCurrentContext(self.entries[self.currentEntry])


    def onBack(self):
        #Exit menuingMode
        self.manager.menuMode = False
