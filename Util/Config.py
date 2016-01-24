import ConfigParser

class Config():

    def __init__(self):
        self.__parser = ConfigParser.RawConfigParser()

    def parseFile(self):
        self.__parser.read('config.ini')

    def writeFile(self):
        self.__parser.add_section('MonitoredParams')
        self.__parser.set('MonitoredParams', 'param1', 'boost')
        self.__parser.set('MonitoredParams', 'param2', 'test')
        self.__parser.set('MonitoredParams', 'param3', 'test1')
        self.__parser.set('MonitoredParams', 'param4', 'test2')

        self.__parser.add_section('RpmThresholds')
        self.__parser.set('RpmThresholds', 'green', '3500')
        self.__parser.set('RpmThresholds', 'orange', '4500')
        self.__parser.set('RpmThresholds', 'red', '5500')
        self.__parser.set('RpmThresholds', 'blue', '6500')

        with open('./Util/config.ini', 'wb') as configFile:
            self.__parser.write(configFile)

