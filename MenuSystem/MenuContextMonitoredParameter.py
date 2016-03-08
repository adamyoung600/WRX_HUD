import Hardware.SH1106.SH1106LCD
from MenuSystem.MenuContext import *


class MenuContextMonitoredParameter(MenuContext):

    def __init__(self, inManager, inLcd):
        super(MenuContextMonitoredParameter,self).__init__(inManager, inLcd)
        self.title = "Monitored Params"     #Title to display at the top of the display when this menu is active.
        self.entries = ["Set Parameters", "Set Passive Mode"]           #Holds a reference to all the possible entries in the menu
        self.parent = "Main"



