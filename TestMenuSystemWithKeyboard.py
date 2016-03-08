from MenuSystem.MenuManager import *
from Hardware.SH1106.SH1106LCD import *
from Hardware.Input.Keyboard import *
from HUDMain import HUDMain




lcd = SH1106LCD()
menuSystem = MenuManager(lcd, None)
menuSystem.initiateDisplay()
menuSystem.enterMenuMode()
keyboard = Keyboard()

while True:
    input_val = keyboard.getChar()
    if input_val == 'w':
        menuSystem.upButtonCallback()
    elif input_val == 's':
        menuSystem.downButtonCallback()
    elif input_val == 'p':
        menuSystem.setButtonCallback()
    elif input_val == 'o':
        menuSystem.backButtonCallback()
    elif input_val == 'q':
        break


