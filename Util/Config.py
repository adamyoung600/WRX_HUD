import ConfigParser

class Config():

    def __init__(self):
        self.__parser = ConfigParser.RawConfigParser()
        self.parseFile()

    def parseFile(self):
        self.__parser.read('config.ini')

    def setDefaultConfig(self):
        if not self.__parser.has_section('MonitoredParams'):
            self.__parser.add_section('MonitoredParams')
        self.__parser.set('MonitoredParams', 'param1', 'P2')
        self.__parser.set('MonitoredParams', 'param2', 'P200')
        self.__parser.set('MonitoredParams', 'param3', 'E20')

        if not self.__parser.has_section('RpmThresholds'):
            self.__parser.add_section('RpmThresholds')
        self.__parser.set('RpmThresholds', 'green', '3500')
        self.__parser.set('RpmThresholds', 'orange', '4500')
        self.__parser.set('RpmThresholds', 'red', '5500')
        self.__parser.set('RpmThresholds', 'blue', '6500')

        with open('./Util/config.ini', 'wb') as configFile:
            self.__parser.write(configFile)

    def setMonitoredParams(self, params):
        self.__parser.set('MonitoredParams', 'param1', params[0])
        self.__parser.set('MonitoredParams', 'param2', params[1])
        self.__parser.set('MonitoredParams', 'param3', params[2])
        with open('./Util/config.ini', 'wb') as configFile:
            self.__parser.write(configFile)

    def getMonitoredParams(self):
        monitoredParams = []
        monitoredParams.append(self.__parser.get('MonitoredParams', 'param1'))
        monitoredParams.append(self.__parser.get('MonitoredParams', 'param2'))
        monitoredParams.append(self.__parser.get('MonitoredParams', 'param3'))
        return monitoredParams

    def setRpmThresholds(self, thresholds):
        self.__parser.set('RpmThresholds', 'green', thresholds[0])
        self.__parser.set('RpmThresholds', 'orange', thresholds[1])
        self.__parser.set('RpmThresholds', 'red', thresholds[2])
        self.__parser.set('RpmThresholds', 'blue', thresholds[3])
        with open('./Util/config.ini', 'wb') as configFile:
            self.__parser.write(configFile)

    def getRpmThresholds(self):
        thresholds = []
        thresholds.append(self.__parser.get('RpmThresholds', 'green'))
        thresholds.append(self.__parser.get('RpmThresholds', 'orange'))
        thresholds.append(self.__parser.get('RpmThresholds', 'red'))
        thresholds.append(self.__parser.get('RpmThresholds', 'blue'))
        return thresholds