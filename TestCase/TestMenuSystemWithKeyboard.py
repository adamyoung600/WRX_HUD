from MenuSystem.MenuManager import MenuManager
from Hardware.SH1106 import SH1106LCD
from Hardware.Input import Keyboard




lcd = SH1106LCD
menuSystem = MenuManager(lcd)
keyboard = Keyboard()

while True:
    input_val = keyboard.getChar()
    if input_val == 'w':
        MenuManager.upButtonCallback()
    elif input_val == 's':
        MenuManager.downButtonCallback()
    elif input_val == 'p':
        MenuManager.setButtonCallback()
    elif input_val == 'o':
        MenuManager.backButtonCallback()
    elif input_val == 'q':
        break


