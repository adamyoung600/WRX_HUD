from GearIndicator import *

"""
Tests the functionality of the gear indicator.
"""

if __name__=="__main__":

    testGearDisplay = GearIndicator()
    while 1:
        testGearDisplay.DisplayNeutral()
        time.sleep(1)
        for i in range(6):
            testGearDisplay.DisplayGear(i)
            time.sleep(1)
