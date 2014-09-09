import Hardware.SH1106.SH1106LCD
from MenuSystem.MenuContext import *


class DtcCodeContext(MenuContext):

    def __init__(self, inManager, inLcd):
        super.__init__(inManager, inLcd)
        self.title = "Engine Trouble Codes"     #Title to display at the top of the display when this menu is active.
        self.entries = []           #Holds a reference to all the possible entries in the menu


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