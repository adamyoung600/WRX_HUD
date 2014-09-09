# from Sh1106.GearIndicatorLCD import *
from Hardware.I2CConfig import *
from Hardware.WideHKOLED.WideHKOLED import *

import traceback
import time




import array
import os
import os.path
import time
import cPickle as pickle

from SSM.pimonitor.PM import PM
from SSM.pimonitor.PMConnection import PMConnection
from SSM.pimonitor.PMPacket import PMPacket
from SSM.pimonitor.PMParameter import PMParameter
from SSM.pimonitor.PMUtils import PMUtils
from SSM.pimonitor.PMXmlParser import PMXmlParser



"""
Used to sample the gear ratio in the car.  Testing purposes.
"""
if __name__=="__main__":
    #Initialize second i2c bus
    i2cConfig()

    testDisplay = WideHKOLED()

    testDisplay.sendString("This is a test", 0, 0)
    testDisplay.sendString("It worked !", 1, 0)



        #Pad out the string
        # if len(rpmString) < 4:
        #     for i in range(0, 3-len(rpmString)):
        #         rpmString = " " + rpmString
        # rpmDisplay.sendString(rpmString, 0, 0)



