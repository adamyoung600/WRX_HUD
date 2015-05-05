import traceback
import time

from SSM.pimonitor.PMConnection import PMConnection
from SSM.pimonitor.PMXmlParser import PMXmlParser
from EngineData.SSM.pimonitor import PMSwitchParser


if __name__=="__main__":
    parser = PMXmlParser()
    switchParser = PMSwitchParser()
    supported_parameters = []
    supported_switches = []
    print "starting parse"
    defined_parameters = parser.parse("logger_METRIC_EN_v131.xml")
    defined_switches = switchParser.parse("logger_METRIC_EN_v131.xml")
    for i in defined_switches:
        print i.to_string()

    print "finished parse"
    connection = PMConnection()

    init_finished = False

    while not init_finished:
        try:
            connection.open()
            #Query ecu/tcu to see which parameters are supported.
            ecu_packet = connection.init(1)
            tcu_packet = connection.init(2)

            if ecu_packet == None or tcu_packet == None:
                print "Can't get initial data."
                continue

            ########################################################################################
            #Match the defined parameters against which ones are in teh ecu/tcu supported parameters
            for p in defined_parameters:
                if (p.get_target() & 0x1 == 0x1) and p.is_supported(ecu_packet.to_bytes()[5:]):
                    if not filter(lambda x: x.get_id() == p.get_id(), supported_parameters):
                        supported_parameters.append(p)

            for p in defined_parameters:
                if ((p.get_target() & 0x2 == 0x2) or (p.get_target() & 0x1 == 0x1)) and p.is_supported(tcu_packet.to_bytes()[5:]):
                    if not filter(lambda x: x.get_id() == p.get_id(), supported_parameters):
                        supported_parameters.append(p)

            for p in defined_parameters:
                p_deps = p.get_dependencies()
                if not p_deps:
                    continue

                deps_found = ()
                for dep in p_deps:
                    deps_found = filter(lambda x: x.get_id() == dep, supported_parameters)
                    if not deps_found:
                        break

                    if len(deps_found) > 1:
                        raise Exception('duplicated dependencies', deps_found)

                    p.add_parameter(deps_found[0])

                if deps_found:
                    supported_parameters.append(p)

            ####################################################################################
            #Match the defined switches against which ones are in teh ecu/tcu supported switches
            for p in defined_switches:
                if (p.get_target() & 0x1 == 0x1) and p.is_supported(ecu_packet.to_bytes()[5:]):
                    if not filter(lambda x: x.get_id() == p.get_id(), supported_switches):
                        supported_switches.append(p)

            for p in defined_switches:
                if ((p.get_target() & 0x2 == 0x2) or (p.get_target() & 0x1 == 0x1)) and p.is_supported(tcu_packet.to_bytes()[5:]):
                    if not filter(lambda x: x.get_id() == p.get_id(), supported_switches):
                        supported_switches.append(p)

            supported_parameters.sort(key=lambda p: int(p.get_id()[1:]), reverse=False)
            supported_switches.sort(key=lambda p: int(p.get_id()[1:]), reverse=False)

            #####################################################################################
            #Print out the parameters and switches
            paramFile = open("supportedParameters","w")
            print "==================================="
            print "Supported Parameters Below:"
            print "==================================="
            #Print out the supported parameters
            for p in supported_parameters:
                paramFile.write(p.to_string())
                paramFile.write('\n')

            switchFile = open("supportedSwitches", "w")
            print "==================================="
            print "Supported Switches Below:"
            print "==================================="
            #Print out the supported parameters
            for s in supported_switches:
                paramFile.write(s.to_string())
                paramFile.write('\n')


            init_finished = True

        except IOError as e:
            traceback.print_exc()
            print "I/O error: {0} {1}".format(e.errno, e.strerror)

            if connection != None:
                connection.close()
                time.sleep(3)
            continue

    connection.close()

