
from Hardware.WideHKOLED.WideHKOLED import WideHKOLED
from Util.ParameterAbbreviations import abbreviations

class DataDisplay():

    def __init__(self):
        self._lcd = WideHKOLED

    def setDisplayTitles(self, paramIDs):
        for i in range(2):
            title = "None"
            if paramIDs[i] in abbreviations:
                title = abbreviations(paramIDs[i])
            self._lcd.sendString(title, i, 0)

    def update(self, newValues):
        for i in range(2):
            tempString = newValues[i]
            # Display only has room for 4 characters per value.
            if len(tempString) > 4:
                tempString = tempString[:4]
            self._lcd.sendStringByEnd(tempString, i, 15)




