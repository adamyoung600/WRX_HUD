from Hardware.ShiftLights import ShiftLights
import time
from GearIndicator import *

lights = ShiftLights([3500, 4000, 5000, 6000])

while True:

    print "Sending 3700"
    testGearDisplay = GearIndicator()
    lights.update(3700)
    time.sleep(0.25)
    testGearDisplay.DisplayGear(0)


    print "Sending 4500"
    lights.update(4500)
    time.sleep(0.25)
    testGearDisplay.DisplayGear(1)

    print "Sending 5500"
    lights.update(5500)
    time.sleep(0.25)
    testGearDisplay.DisplayGear(2)

    print "Sending 6500"
    lights.update(6500)
    time.sleep(0.25)
    testGearDisplay.DisplayGear(3)

    print "Clearing lights"
    lights._clearLights()
    time.sleep(0.5)
    testGearDisplay.DisplayNeutral()
