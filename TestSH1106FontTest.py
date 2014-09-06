from Hardware.SH1106.SH1106LCD import *
from Hardware.I2CConfig import *
from Hardware.SH1106.SH1106FontLib import *

i2cConfig()
lcd = SH1106LCD()
lcd.displayString("This is a test!", 0, 0)
lcd.displayString("Skip a row, please", 2, 10)
lcd.displayString("@#$%^&*()-_=+,.<>", 4,0)
lcd.clearScreen()
lcd.displayString("This is to test the text wrapping ability of my super awesome LCD screen", 5, 0)

