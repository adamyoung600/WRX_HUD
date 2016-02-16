from Hardware.ShiftLights import ShiftLights
import time

lights = ShiftLights([3500, 4000, 5000, 6000])

while True:
    print "Sending 3000"
    lights.update("3000")
    time.sleep(1)

    print "Sending 3700"
    lights.update("3700")
    time.sleep(1)

    print "Sending 4500"
    lights.update("4500")
    time.sleep(1)

    print "Sending 5500"
    lights.update("5500")
    time.sleep(1)

    print "Sending 6500"
    lights.update("6500")
    time.sleep(1)

    print "Clearing lights"
    lights._clearLights()
    time.sleep(4)
