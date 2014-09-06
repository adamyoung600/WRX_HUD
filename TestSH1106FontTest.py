from Hardware.SH1106.SH1106LCD import *
from Hardware.I2CConfig import *
from Hardware.SH1106.SH1106FontLib import *

i2cConfig()
lcd = SH1106LCD()
lcd.displayInvertedString("Test inversion", 0, 0)
lcd.displayString("In between", 1, 0)
lcd.displayInvertedString("Second Test", 2, 0)
lcd.displayString("This is to test the text wrapping ability of my super awesome LCD screen", 5, 0)

