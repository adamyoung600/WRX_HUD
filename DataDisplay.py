
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



