import serial
import string
import time

class ObdConnection(object):

    def __init__(self):
        self._ser = None

    def open(self):
        self._ser = serial.Serial(
                            port='/dev/ttyUSB0',
                            baudrate=9600,
                            timeout=2000,
                            writeTimeout=55,
                            parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE,
                            bytesize=serial.EIGHTBITS)
        time.sleep(0.2)

    def close(self):
        if self._ser != None:
            self._ser.close()

    def init


    def send_command(self, cmd):
        if self._ser:
            self._ser.flushOutput()
            self._ser.flushInput()
            for c in cmd:
                self._ser.write(c)
            self._ser.write("\r\n")

    def interpret_result(self, code):
        if len(code) < 7:
            raise "BogusCode"

        #Get the first thing returned
        code = string.split(code, "\r")
        code = code[0]

        #Remove whitespace
        code = string.split(code)
        code = string.join(code, "")

        if code[:6] == "NODATA":
            return "NODATA"

        #First 4 characters are code from obd
        code = code[4:]
        return code