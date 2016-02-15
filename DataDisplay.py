
from Hardware.WideHKOLED.WideHKOLED import WideHKOLED
from Util.ParameterAbbreviations import abbreviations

class DataDisplay():

    def __init__(self):
        self._lcd = WideHKOLED

    def setDisplayTitles(self, paramIDs):
        for i in range(3):
            title = "None"
            if paramIDs[i] in abbreviations:
                title = abbreviations('paramIDs[i]')
            self._lcd.sendString(title, 0, i*6)

    def update(self, newValues):
        for i in range(3):
            tempString = newValues[i]
            # Display only has room for 4 characters per value.  Must be this size.
            if len(tempString) > 4:
                tempString = tempString[:4]
            elif len(tempString) < 4:
                # Pad it to 4 characters using leading whitespace
                for i in range(0, 3-len(tempString)):
                    tempString = " " + tempString




