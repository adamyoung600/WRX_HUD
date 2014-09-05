from Hardware.SH1106.SH1106LCD import *
from Hardware.I2CConfig import *



class GearIndicator():

    def __init__(self):
        #Set up second I2C bus
        i2cConfig()
        self.lcd = SH1106LCD()

        #Import startup image from disk.
        self.image_path = os.chdir("Hardware")

        self.lcd.addImage("FirstGear", "shift_1_sized.bmp")
        self.lcd.addImage("SecondGear", "shift_2_sized.bmp")
        self.lcd.addImage("ThirdGear", "shift_3_sized.bmp")
        self.lcd.addImage("FourthGear", "shift_4_sized.bmp")
        self.lcd.addImage("FifthGear", "shift_5_sized.bmp")
        self.lcd.addImage("Reverse", "shift_R_sized.bmp")
        self.lcd.addImage("Neutral", "shift_N_sized.bmp")
        self.lcd.addImage("SubaruLogo", "subie_logo.bmp")
        self.lcd.addImage("WrxLogo", "wrx_logo.bmp")
        self.lcd.displayBufferedImage("SubaruLogo", 0, 0)
        time.sleep(2)
        self.lcd.displayBufferedImage("WrxLogo", 0, 0)
        time.sleep(2)
        self.lcd.clearScreen()


    def DisplayGear(self, gear):
        try:
            #Determine which image to display
            if gear==0:
                image_data = self.lcd.displayBufferedImage("Reverse", 0, 50)
            elif gear==1:
                image_data = self.lcd.displayBufferedImage("FirstGear", 0, 50)
            elif gear==2:
                image_data = self.lcd.displayBufferedImage("SecondGear", 0, 50)
            elif gear==3:
                image_data = self.lcd.displayBufferedImage("ThirdGear", 0, 50)
            elif gear==4:
                image_data = self.lcd.displayBufferedImage("FourthGear", 0, 50)
            elif gear==5:
                image_data = self.lcd.displayBufferedImage("FifthGear", 0, 50)
            else:
                raise ValueError("Gear selection must be within 0 to 5.")

        except ValueError as e:
            print "Value Error: "
            traceback.print_exc()

    def DisplayNeutral(self):
        self.lcd.displayBufferedImage("Neutral", 0, 50)

    def ClearScreen(self):
        self.lcd.clearScreen()
