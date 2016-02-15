'''
Feb 2016
@author: Adam Young
'''

import time

from SSM.pimonitor.PMConnection import PMConnection
from SSM.pimonitor.PMXmlParser import PMXmlParser

class EcuData():

    def __init__(self):
        #Create connection to the ECU using SSM protocol
        ecuid = "1B04400405" #TODO: replace this with a call to query the ecu id.
        parser = PMXmlParser(ecuid)
        self.supported_parameters = {}
        self.defined_parameters = parser.parse("logger_METRIC_Condensed_v131.xml")
        self.connection = PMConnection()
        self.__initConnection__()
        #Init core parameters
        self.coreParametersReady = False
        self.wheelSpeedParameter = None
        self.engineSpeedParameter = None
        self.monitoredParameters = None

        self.__initCoreParameters()

    """####################################################
    Initialization methods - Start
    ####################################################"""

    def __initConnection__(self):

        #Initialize the connection
        init_finished = False

        while not init_finished:
            try:
                print "Trying to establish connection to ecu."
                self.connection.open()
                #Query ecu/tcu to see which parameters are supported.
                ecu_packet = self.connection.init(1)
                tcu_packet = self.connection.init(2)

                if ecu_packet == None or tcu_packet == None:
                    print "Can't get initial data."
                    continue

                #Match the defined parameters against which ones are in teh ecu/tcu supported parameters
                for p in self.defined_parameters:
                    if (p.get_target() & 0x1 == 0x1) and p.is_supported(ecu_packet.to_bytes()[5:]):
                        if not filter(lambda x: x.get_id() == p.get_id(), self.supported_parameters.values()):
                            self.supported_parameters[p.get_id] = p

                for p in self.defined_parameters:
                    if ((p.get_target() & 0x2 == 0x2) or (p.get_target() & 0x1 == 0x1)) and p.is_supported(tcu_packet.to_bytes()[5:]):
                        if not filter(lambda x: x.get_id() == p.get_id(), self.supported_parameters.values()):
                            self.supported_parameters[p.get_id] = p

                for p in self.defined_parameters:
                    p_deps = p.get_dependencies()
                    if not p_deps:
                        continue

                    deps_found = ()
                    for dep in p_deps:
                        deps_found = filter(lambda x: x.get_id() == dep, self.supported_parameters.values())
                        if not deps_found:
                            break

                        if len(deps_found) > 1:
                            raise Exception('duplicated dependencies', deps_found)

                        p.add_parameter(deps_found[0])

                    if deps_found:
                        self.supported_parameters[p.get_id] = p

                # each ID must be in a form P01 - first letter, then a number
                #self.supported_parameters.sort(key=lambda p: int(p.get_id()[1:]), reverse=False)

                init_finished = True
                print "Connection initialized."

            except IOError as e:
                print "I/O error: {0} {1}".format(e.errno, e.strerror)

                if self.connection != None:
                    self.connection.close()
                    time.sleep(3)
                continue

    def setMonitoredParams(self, paramIDs):
        for id in paramIDs:
            for p in self.supported_parameters.keys():
                if p.get_id() == id:
                    self.monitoredParameters.append(p)

    def getMonitoredParams(self):
        packets = self.connection.read_parameters(self.monitoredParameters)
        currentValues = []
        for i in range(len(packets)):
            currentValues.append(self.monitoredParameters[i].get_value(packets[i]))
        return currentValues


    def __initCoreParameters__(self):
        pass

    """####################################################
    Initialization methods - End
    ####################################################"""

    """####################################################
    Core Parameter Queries - Start
    ####################################################"""
    def _getParamByID(self, id):
        if id in self.supported_parameters.keys():
            parameter = self.supported_parameters[id]
            response = self.connection.read_parameter(parameter)
            return parameter.get_value(response)
        else:
            return None

    def _getParamListByID(self, ids):
        validParams = []
        for id in ids:
            if id in self.supported_parameters.keys():
                validParams.append(self.supported_parameters[id])
        if validParams:     # List not empty
            responses = self.connection.read_parameters(validParams)
            values = []
            for i in range(len(responses)):
                values.append(validParams[1].get_value(responses[i]))
            return values
        else:
            return None

    def getEngineSpeed(self):
        pass

    def getCurrentGear(self):
        pass

    def isInGear(self):
        pass

    def getThrottlePosition(self):
        pass