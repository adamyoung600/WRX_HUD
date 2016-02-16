import smbus  #Library is specific to the python distribution on Raspbian Linux
import time

#declare i2c specifics

OLED_Address = 0x3c
OLED_Command_Mode = 0x80
OLED_Data_Mode = 0x40

"""
Class WideHKOLED

Interface to the 16x2 OLED display sold by the ebay user wide-hk.
"""
class WideHKOLED():
    def __init__(self):
        self.__bus = smbus.SMBus(0)
        self.__initialize()

    """
    Most of this was stripped from the sample arduino code that
    wide-hk provides when you buy one of the LCDs.
    """
    def __initialize(self):
        time.sleep(1)
        self.__sendCommand(0x2A)
        self.__sendCommand(0x71)
        self.__sendCommand(0x5C)
        self.__sendCommand(0x28)
    
        self.__sendCommand(0x08)	
        self.__sendCommand(0x2A)	# **** Set "RE"=1	00101010B
        self.__sendCommand(0x79)	# **** Set "SD"=1	01111001B
    
        self.__sendCommand(0xD5)
        self.__sendCommand(0x70)
        self.__sendCommand(0x78)	# **** Set "SD"=0  01111000B
    
        self.__sendCommand(0x08)	# **** Set 5-dot, 3 or 4 line(0x09), 1 or 2 line(0x08)
    
        self.__sendCommand(0x06)	# **** Set Com31-->Com0  Seg0-->Seg99
    
        # **** Set OLED Characterization *** #
        self.__sendCommand(0x2A) 	# **** Set "RE"=1 
        self.__sendCommand(0x79)  	# **** Set "SD"=1
    
        # **** CGROM/CGRAM Management *** #
        self.__sendCommand(0x72)  	# **** Set ROM
        self.__sendCommand(0x00)  	# **** Set ROM A and 8 CGRAM
    
    
        self.__sendCommand(0xDA) 	# **** Set Seg Pins HW Config
        self.__sendCommand(0x10)   
    
        self.__sendCommand(0x81)  	# **** Set Contrast
        self.__sendCommand(0xFF) 
    
        self.__sendCommand(0xDB)  	# **** Set VCOM deselect level
        self.__sendCommand(0x30)  	# **** VCC x 0.83
    
        self.__sendCommand(0xDC)  	# **** Set gpio - turn EN for 15V generator on.
        self.__sendCommand(0x03)
    
        self.__sendCommand(0x78)  	# **** Exiting Set OLED Characterization
        self.__sendCommand(0x28) 
        self.__sendCommand(0x2A) 

        self.__sendCommand(0x06) 	# **** Set Entry Mode
        self.__sendCommand(0x08)  
        self.__sendCommand(0x28) 	# **** Set "IS"=0 , "RE" =0 #28
        self.__sendCommand(0x01) 
        self.__sendCommand(0x80) 	# **** Set DDRAM Address to 0x80 (line 1 start)
    
        time.sleep(0.1)
        self.powerUp()	# Turn on display
    
    """
    powerUp()

    Powers on the LCD.  Will continue to display whatever was sent to the
    LCD last.
    """
    def powerUp(self):
        time.sleep(1)
        self.__sendCommand(0x0C)

    """"
    powerDown()

    Turn off the LCD.  Does not "forget" what was on the screen.  It
    will be displayed again the next time the LCD is powered up.
    """
    def powerDown(self):
        time.sleep(1)
        self.__sendCommand(0x08)	# Power off display

    """
    clearScreen()

    Wipes whatever was being displayed on the LCD.  This is a
    built in feature of the LCD.
    """
    def clearScreen(self):
        self.__sendCommand(0x01)

    """
    setCursorPostion (row, col)

        row - Row to place the cursor (0 or 1)
        col - Column to place the cursor (0 to 15)

    Sets the current cursor position.  The LCD will place the next character
    sent to the LCD at the cursor position and automatically move the cursor
    to the next position allowing for continuous streaming of data.
    """
    def setCursorPosition(self, row, col):
        #TODO: check the limits of row/col here and throw an error.
        rowOffsets = [0x00, 0x40]
        baseOffset = 0x80
        position = baseOffset + rowOffsets[row] + col
        self.__sendCommand(position)
        time.sleep(0.005)

    """
    __sendCommand(command)
    
        command - Hex data to send to the OLED as a command
    
    Used to send data to the OLED that should be interpreted as a command, and not display data.
    Commands are used to control the functions/configuration of the OLED.
    This method sends the control byte with the D/C Bit set LOW to tell the OLED that the next
    data sent will be a command
    """
    def __sendCommand(self, command):
        self.__bus.write_byte_data(OLED_Address, OLED_Command_Mode, command)
        time.sleep(0.005)
        
    """
    __sendData(data)
    
        data - Hex data to send to the OLED as display data

    Sends data to the OLED that is to be interpreted as display data.  Sends the control byte
    with the D/C Bit set HIGH to tell the OLED that the data is display data.
    """
    def __sendData(self, data):
        self.__bus.write_byte_data(OLED_Address, OLED_Data_Mode, data)
        time.sleep(0.005)
    
    """
    sendString(text, row, col)
    
        text - The string that you want to display
        row - The row on which to begin printing the string (0 is upper, 1 is lower)
        col - the position within the row to start printing the string (0 to 15)
    
    Sends a string to the lcd to be placed at the cursor position indicated
    """
    def sendString(self, text, row, col):
        #TODO: error checking to make sure the text will either wrap or not accept something that's too long.
        self.setCursorPosition(row, col)
        for char in text:
            self.__sendData(int(hex(ord(char)), 16))

    """
    sendStringByEnd(text, row, colEndPosition)

        text - The string that you want to display
        row - The row on which to begin printing the string (0 is upper, 1 is lower)
        colEndPosition - The position on which the last character of the string should appear

    Sends a string to the lcd placing the LAST character of the string at the indicated position.
    """
    def sendStringByEnd(self, text, row, colEndPosition):
        if len(text) > colEndPosition+1:
            self.setCursorPosition(row, 0)
            text = text[:4]
        else:
            self.setCursorPosition(row, colEndPosition-len(text))

        for char in text:
            self.__sendData(int(hex(ord(char)), 16))

