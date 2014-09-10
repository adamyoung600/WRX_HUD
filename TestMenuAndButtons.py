from Hardware.SH1106.SH1106LCD import *
from Hardware.Input.Keypad import *
from MenuSystem.MenuManager import *

lcd = SH1106LCD()
menu = MenuManager(lcd)
keypad = Keypad(menu)

while True:
    pass
