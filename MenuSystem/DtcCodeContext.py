import Hardware.SH1106.SH1106LCD
from MenuSystem.MenuContext import *


class DtcCodeContext(MenuContext):

    def __init__(self, inManager, inLcd):
        super(DtcCodeContext, self).__init__(inManager, inLcd)
        self.title = "Engine Trouble Codes"     #Title to display at the top of the display when this menu is active.
        self.entries = []           #Holds a reference to all the possible entries in the menu


    """
    Callback methods that perform an action for a button press based on which menu the user is in.
    """
    def onUp(self):
        pass
    def onDown(self):
        pass
    def onSet(self):
        pass
    def onBack(self):
        pass