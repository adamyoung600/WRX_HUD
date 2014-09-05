from Hardware.SH1106.SH1106LCD import *
from Hardware.I2CConfig import *
from Hardware.SH1106.SH1106FontLib import *

i2cConfig()
lcd = SH1106LCD()
time.sleep(1)
lcd.setCursorPosition(0, 0)
time.sleep(1)
myFont = font2
for i in myFont:
    lcd.sendDataByte(0x00)
    lcd.sendData(i)


