import Hardware.SH1106.SH1106LCD
from MenuSystem.MenuContext import *


class MainMenuContext(MenuContext):

    def __init__(self, inManager, inLcd):
        super(MainMenuContext, self).__init__(inManager, inLcd)
        self.title = "Main"         #Title to display at the top of the display when this menu is active.
        self.entries = ["SSM Parameters", "Peak Boost", "Test1", "Test2"]           #Holds a reference to all the possible entries in the menu
        self.isSet = [False, False, False, False]

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
        #Wipe arrow on the last line
        self.lcd.displayString(" ", self.lastEntry+2, 5)
        #Point arrow to new line
        self.lcd.displayString(">", self.currentEntry+2, 5)

    """
    Callback methods that perform an action for a button press based on which menu the user is in.
    Need to be implemented by child classes
    """
    def onUp(self):
        if self.currentEntry > 0:
            print "Up"
            self.lastEntry = self.currentEntry
            self.currentEntry -= 1
            self.updateDisplay()

    def onDown(self):
        if self.currentEntry < len(self.entries)-1:
            print "Down"
            self.lastEntry = self.currentEntry
            self.currentEntry += 1
            self.updateDisplay()

    def onSet(self):
        print "Set"
        if not self.isSet[self.currentEntry]:
            self.lcd.displayString("*", self.currentEntry+2, 11)
            self.isSet[self.currentEntry] = True
        else:
            self.lcd.displayString(" ", self.currentEntry+2, 11)
            self.isSet[self.currentEntry] = False
    def onBack(self):
        pass