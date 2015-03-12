import Hardware.SH1106.SH1106LCD



class MenuContext(object):

    def __init__(self, inManager, inLcd):
        self.manager = inManager
        self.lcd = inLcd            #Reference to the LCD on which to display the menu
        self.title = "No Title"     #Title to display at the top of the display when this menu is active.
        self.entries = []           #Holds a reference to all the possible entries in the menu
        self.currentEntry = 0       #Index to the current entry in the menu that should be highlighted.  Defaults to the first entry.
        self.lastEntry = 0          #Index to the last entry that was highlighted.

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


