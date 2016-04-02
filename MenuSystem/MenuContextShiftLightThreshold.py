from MenuSystem.MenuContext import *


class MenuContextShiftLightThreshold(MenuContext):

    def __init__(self, inManager, inLcd, inTitle, inThresholdNum):
        super(MenuContextShiftLightThreshold, self).__init__(inManager, inLcd)
        self.title = inTitle        #Title to display at the top of the display when this menu is active.
        self.parent = "Shift Lights"
        self.thresholdNum = inThresholdNum
        self.threshold = self.manager.getShiftLightThreshold(self.thresholdNum)

    """
    Used to display the menu data on the LCD
    """
    def initDisplay(self):
        self.lcd.clearScreen()
        #Display title
        self.lcd.displayString(self.title, 0, 0)
        self.lcd.displayString("---------------------", 1, 0)
        #Display options
        self.lcd.centerString(self.threshold, 4)

    """
    Used to display the current list items on the screen
    """
    def updateValue(self):
        self.lcd.clearRow(4)
        self.lcd.centerString(self.threshold, 4)
    """
    Callback methods that perform an action for a button press based on which menu the user is in.
    Need to be implemented by child classes
    """
    def onUp(self):
        if self.threshold < 6500:
            self.threshold+=100
            self.updateValue()

    def onDown(self):
        if self.threshold > 100:
            self.threshold-=100
            self.updateValue()

    def onSet(self):
        self.manager.setShiftLightThreshold(self.thresholdNum, self.threshold)
        self.displayMessage("Set to: " + str(self.threshold))
