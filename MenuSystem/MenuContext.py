import Hardware.SH1106.SH1106LCD
import time



class MenuContext(object):

    def __init__(self, inManager, inLcd):
        self.manager = inManager
        self.lcd = inLcd            #Reference to the LCD on which to display the menu
        self.title = "No Title"     #Title to display at the top of the display when this menu is active.
        self.entries = []           #Holds a reference to all the possible entries in the menu
        self.currentEntry = 0       #Index to the current entry in the menu that should be highlighted.  Defaults to the first entry.
        self.lastEntry = 0          #Index to the last entry that was highlighted.
        self.parent = None

    """
    Used to display the menu data on the LCD
    """
    def initDisplay(self):
        self.lcd.clearScreen()
        #Display title
        self.lcd.displayString(self.title, 0, 0)
        self.lcd.displayString("---------------------", 1, 0)
        #Display options
        for i in range(0, len(self.entries)):
            #wipe any old arrows
            self.lcd.displayString(" ", i+2, 5)
            #place text for entry
            self.lcd.displayString(self.entries[i], i+2, 17)
        #Set new arrow to current selection
        self.lcd.displayString(">", 2, 5)
        self.currentEntry = 0

    """
    Called to update the display after input has been processed
    """
    def updateDisplay(self):
        #Wipe arrow on the last line
        self.lcd.displayString(" ", self.lastEntry+2, 5)
        #Point arrow to new line
        self.lcd.displayString(">", self.currentEntry+2, 5)

    """
    Called to wipe the menu options and display a message for 1 second.  Automatically redraws the menu.
    """
    def displayMessage(self, inString):
        self.lcd.clearScreen()
        self.lcd.centerString(inString, 3)
        time.sleep(1)
        self.initDisplay()


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
        if len(self.entries > self.currentEntry):
            self.manager.setCurrentContext(self.entries[self.currentEntry])

    def onBack(self):
        if self.parent:
            self.manager.setCurrentContext(self.parent)


