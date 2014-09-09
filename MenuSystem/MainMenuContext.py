import Hardware.SH1106.SH1106LCD
from MenuSystem.MenuContext import *


class MainMenuContext(MenuContext):

    def __init__(self, inManager, inLcd):
        super.__init__(inManager, inLcd)
        self.title = "Main"         #Title to display at the top of the display when this menu is active.
        self.entries = ["Monitored SSM Parameters", "Peak Boost"]           #Holds a reference to all the possible entries in the menu


    """
    Used to display the menu data on the LCD
    """
    def initDisplay(self):
        self.lcd.displayString(self.title, 0, 0)
        self.lcd.displayString("-----------------------------------", 1, 0)
        self.lcd.displayInvertedString(self.entries[0], 2, 15)
        for i in range(1, len(self.entries) - 1):
            self.lcd.displayString[self.entries[i], i+1, ]
        self.lcd.displayString(">", 2, 5)

    def updateDisplay(self):
        pass

    """
    Callback methods that perform an action for a button press based on which menu the user is in.
    Need to be implemented by child classes
    """
    def onUp(self):
        pass
    def onDown(self):
        pass
    def onSet(self):
        pass
    def onBack(self):
        pass