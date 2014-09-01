from GearIndicator import *

"""
Tests the functionality of the gear indicator.
"""

if __name__=="__main__":

    testGearDisplay = GearIndicator()
    while 1:
        testGearDisplay.DisplayNeutral()
        time.sleep(1)
        for i in range(5):
            testGearDisplay.DisplayGear(i+1)
            time.sleep(1)
