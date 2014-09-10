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
        pass
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


