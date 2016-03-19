import Hardware.SH1106.SH1106LCD
from MenuSystem.MenuContext import *
from Util.ParameterAbbreviations import abbreviations


class MenuContextParameterSelectionList(MenuContext):

    def __init__(self, inManager, inLcd, inParamNum):
        super(MenuContextParameterSelectionList, self).__init__(inManager, inLcd)
        self.title = "Select Parameter"         #Title to display at the top of the display when this menu is active.
        self.entries = abbreviations.values()           #Holds a reference to all the possible entries in the menu
        self.parent = "Set Parameters"
        self.oldtopEntry = 0
        self.newTopEntry = 0
        self.paramNumber = inParamNum

    """
    Used to display the menu data on the LCD
    """
    def initDisplay(self):
        self.lcd.clearScreen()
        #Display title
        self.lcd.displayString(self.title, 0, 0)
        self.lcd.displayString("---------------------", 1, 0)
        #Display options
        for i in range(6):
            #wipe any old arrows
            self.lcd.displayString(" ", i+2, 5)
            #place text for entry
            self.lcd.displayString(self.entries[i], i+2, 17)
        #Set new arrow to current selection
        self.lcd.displayString(">", 2, 5)
        self.currentEntry = 0

    """
    Used to display the current list items on the screen
    """
    def updateList(self):
        endEntry = None
        if self.newTopEntry + 6 > len(self.entries) - 1:
            endEntry = len(self.entries)
        else:
            endEntry = self.newTopEntry + 6

        #Clear the lines
        for i in range(2,8):
            #Clear all the lines
            self.lcd.clearRow(i)

        #Display the new options
        row = 2
        for j in range(self.newTopEntry, endEntry):
            self.lcd.displayString(self.entries[j], row, 17)
            row += 1

    """
    Called to update the display after input has been processed
    """
    def updateDisplay(self):
        if self.newTopEntry != self.oldtopEntry:
            #Update the listed items
            self.updateList()
            self.oldtopEntry = self.newTopEntry
        else:
            #Wipe the old arrow
            self.lcd.displayString(" ", 2 + (self.lastEntry-self.newTopEntry), 5)

        #Display the new arrow
        self.lcd.displayString(">", 2 + (self.currentEntry-self.newTopEntry) , 5)

    """
    Callback methods that perform an action for a button press based on which menu the user is in.
    Need to be implemented by child classes
    """
    def onUp(self):
        if self.currentEntry > self.newTopEntry:
            self.lastEntry = self.currentEntry
            self.currentEntry -= 1
        else:
            if self.newTopEntry > 0:
                #Scroll up the list
                self.newTopEntry -= 1
                self.currentEntry -= 1

        self.updateDisplay()

    def onDown(self):
        if self.currentEntry < self.newTopEntry + 5:
            self.lastEntry = self.currentEntry
            self.currentEntry += 1
        else:
            if self.newTopEntry + 6 < len(self.entries):
                #Scroll down the list
                self.newTopEntry += 1
                self.currentEntry += 1

        self.updateDisplay()

    def onSet(self):
        id = abbreviations.keys()[self.currentEntry]
        self.manager.setMonitoredParam(id, self.paramNumber)
        self.manager.updateMonitoredParameters()
        self.displayMessage("Param Set")