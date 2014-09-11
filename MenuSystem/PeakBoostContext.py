import Hardware.SH1106.SH1106LCD
from MenuSystem.MenuContext import *


class PeakBoostContext(MenuContext):

    def __init__(self, inManager, inLcd):
        super(PeakBoostContext, self).__init__(inManager, inLcd)
        self.title = "Peak Boost"     #Title to display at the top of the display when this menu is active.
        self.entries = ["Display Peak Boost", "Reset Peak Boost"]           #Holds a reference to all the possible entries in the menu


    """
    Used to display the menu data on the LCD
    """
    def initDisplay(self):
        self.lcd.displayString(self.title, 0, 0)
        self.lcd.displayString("--------------------------------", 1, 0)
        for i in range(0, len(self.entries)):
            self.lcd.displayString(self.entries[i], i+2, 17)
        self.lcd.displayString(">", 2, 5)

    def updateDisplay(self):
        pass

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
            self.displayBoost()
        elif self.currentEntry==1:
            self.resetBoost()

    def onBack(self):
        self.manager.setCurrentContext("Main Menu")

    def displayBoost(self):
        pass

    def resetBoost(self):
        pass