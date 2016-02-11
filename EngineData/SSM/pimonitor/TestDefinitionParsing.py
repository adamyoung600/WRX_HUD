import traceback
import time

from EngineData.SSM.pimonitor.PMXmlParser import PMXmlParser
from EngineData.SSM.pimonitor.PMSwitchParser import PMSwitchParser


if __name__=="__main__":
    ecuid = "1B04400405"
    parser = PMXmlParser(ecuid)
    switchParser = PMSwitchParser()
    supported_parameters = []
    supported_switches = []

    print "starting parse of parameters"
    defined_parameters = parser.parse("logger_METRIC_Condensed_v131.xml")
    print "============================="
    for i in defined_parameters:
        print i.to_string()

    print "starting parse of switches"
    defined_switches = switchParser.parse("logger_METRIC_Condensed_v131.xml")
    print "============================="
    for i in defined_switches:
        print i.to_string()

    print "finished parse"


