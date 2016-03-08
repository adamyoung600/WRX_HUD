import Hardware.SH1106.SH1106LCD
from MenuSystem.MenuContext import *
from MenuSystem.MenuContextParameterSelectionList import MenuContextParameterSelectionList


class MenuContextSetParameters(MenuContext):

    def __init__(self, inManager, inLcd):
        super(MenuContextSetParameters, self).__init__(inManager, inLcd)
        self.title = "Set Parameters"         #Title to display at the top of the display when this menu is active.
        self.entries = ["Parameter 1", "Parameter 2"]           #Holds a reference to all the possible entries in the menu
        self.parent = "Monitored Parameters"
    """
    Callback methods that perform an action for a button press based on which menu the user is in.
    """

    def onSet(self):
        if self.currentEntry==0:
            self.manager.setContextDirectly(MenuContextParameterSelectionList(self.manager, self.lcd, 0))
        elif self.currentEntry==1:
            self.manager.setContextDirectly(MenuContextParameterSelectionList(self.manager, self.lcd, 1))


