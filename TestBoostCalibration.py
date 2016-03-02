from Hardware.BoostGauge import BoostGauge
from Hardware.Input.Keyboard import Keyboard

boost = BoostGauge()
keyboard = Keyboard()

while True:
    if(keyboard.getChar() == 'w'):
        boost.calibrate()