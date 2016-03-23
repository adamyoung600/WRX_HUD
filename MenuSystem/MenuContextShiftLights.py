from MenuSystem.MenuContext import *
from MenuSystem.MenuContextShiftLightThreshold import *


class MenuContextShiftLights(MenuContext):

    def __init__(self, inManager, inLcd):
        super(MenuContextShiftLights, self).__init__(inManager, inLcd)
        self.title = "Shift Lights"         #Title to display at the top of the display when this menu is active.
        self.entries = ["Yellow 1", "Yellow 2", "Red", "Blue"]           #Holds a reference to all the possible entries in the menu
        self.parent = "Settings"
    """
    Callback methods that perform an action for a button press based on which menu the user is in.
    """

    def onSet(self):
        if self.currentEntry >= 0 and self.currentEntry < 4:
            self.manager.setCurrentContextDirectly(MenuContextShiftLightThreshold(self.manager, self.lcd, self.entries[self.currentEntry], self.currentEntry))
