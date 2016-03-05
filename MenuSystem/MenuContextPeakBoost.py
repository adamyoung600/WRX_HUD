import Hardware.SH1106.SH1106LCD
from MenuSystem.MenuContext import *


class MenuContextPeakBoost(MenuContext):

    def __init__(self, inManager, inLcd):
        super(MenuContextPeakBoost, self).__init__(inManager, inLcd)
        self.title = "Peak Boost"     #Title to display at the top of the display when this menu is active.
        self.entries = ["Display Peak Boost", "Reset Peak Boost"]           #Holds a reference to all the possible entries in the menu


    """
    Callback methods that perform an action for a button press based on which menu the user is in.
    Need to be implemented by child classes
    """

    def onSet(self):
        if self.currentEntry==0:
            self.displayBoost()
        elif self.currentEntry==1:
            self.resetBoost()

    def onBack(self):
        self.manager.setCurrentContext("Main Menu")

    def displayBoost(self):
        pass

    def resetBoost(self):
        pass