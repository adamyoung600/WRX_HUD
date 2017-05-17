'''
Feb 2016
@author: Adam Young
'''
import threading

import time
import thread
import logging

from SSM.pimonitor.PMConnection import PMConnection
from SSM.pimonitor.PMXmlParser import PMXmlParser



class EcuData():

    def __init__(self):
        self._logFile = logging.getLogger("root")
        #Create connection to the ECU using SSM protocol
        ecuid = "1B04400405" #TODO: replace this with a call to query the ecu id.
        parser = PMXmlParser(ecuid)
        self.supported_parameters = {}
        self.defined_parameters = parser.parse("logger_METRIC_Condensed_v131.xml")
        self.connection = PMConnection()
        self.initConnection()
        #Init core parameters
        self.wheelSpeedParameter = None
        self.engineSpeedParameter = None

        #Monitored Parameters are the three that will be actively monitored on the steering wheel column lcd
        self._monitoredParamIds = None
        self._monitoredParams = None
        self._monitoredParamData = None

        #Core Parameters are the ones that have to be queried no matter what as they control the flow of logic for the main loop
        self._coreParamsIds = ['E25',  #Gear Selection
                            'S4',   #Neutral Switch
                            'S23',  #Clutch Switch
                            'P30',  #Pedal Angle
                            'E11',  #Feedback Knock Control
                            'E1',   #IAM
                            'P8']   #RPM
        self._coreParams = lookupParams(self._coreParamsIds) #dictionary of parameters keyed by ID
        self._coreParamData = dict((element,0) for element in self._coreParamIds)    #dictionary of parameter values keyed by ID

        #Log Parameters are only polled during a WOT pull.
        self._logParamIds = ['P3',    #Air/Fuel Correction
                           'P30',   #Pedal Angle
                           'P200',  #Engine Load
                           'P8',    #RPM
                           'E11',   #FBKC
                           'E12',   #FLKC
                           'E1',    #IAM
                           'P10',   #Ignition Total Timing
                           'P201',  #Injector Duty Cycle
                           'E20',   #Boost
                           'E5',    #Boost Error
                           'P12']    #MAF
        self._logParams = lookupParams(self._logParamIds) #dictionary of parameters keyed by ID
        self._logParamData = dict((element,0) for element in self._logParamIds)  #dictionary of parameter values keyed by ID


    """####################################################
       Externally facing methods
    ####################################################"""


    def setMonitoredParams(self, paramIds):
        """
        setMonitoredParams(paramIds) - Sets the parameters to be monitored by the steering wheel column lcd (maximum of 3).
            paramIds - tuple of SSM IDs representing the parameters we would like to monitor.
        """
        # Reset all old values
        self._monitoredParamIds = paramIds
        self._monitoredParams = []
        self._monitoredParamData = none

        # Lookup parameters based on their IDs
        if len(paramIDs) > 3:
            self._logFile.error("Cannot monitor more than 3 parameters.")
            return
        for id in paramIDs:
            for p in self.supported_parameters.keys():
                if p.get_id() == id:
                    self.monitoredParameters.append(p)
        if len(self._monitoredParams) > 0:
            self._monitoredParamData = dict((element, 0) for element in self._monitoredParamIds)

    def getMonitoredParamValues(self):
        return self._monitoredParamData

    def refreshData(self, wotLogEnabled):
        """
        refreshData(wotLogEnabled) - Make superset of all parameters that need updating and query the ECU for current values.
            wotLogEnabled - Boolean indicating that we are currently in the middle of a WOT log so we should ensure we query
                the ECU for the log parameters

        """
        #Build superset
        superset = self._coreParams.copy()
        superset.update(self._monitoredParams)
        if wotLogEnabled:
            superset.update(self.logParams)
        #Query ECU
        packets = self.connection.read_parameters(superset)
        #Update values
        for i in range(len(packets)):
            id = superset[i].get_id()
            value = superset[i].get_value(packets[i])
            if id in self._coreParamData:
                self._coreParamData[id] = value
            if id in self._monitoredParamData:
                self._monitoredParamData[id] = value
            if id in self._logParamData:
                self._logParamData[id] = value

    def getEngineSpeed(self):
        return self._coreParamData["P8"]

    def getCurrentGear(self):
        return self._coreParamData["E25"]

    def getThrottlePedalAngle(self):
        return self._coreParamData["P13"]

    def isInGear(self):
        # Check Neutral Switch (S4) and Clutch Switch (S63)
        return self._coreParamData["S4"] == "0" and self._coreParamData["S63"] == "0"

    def getParamByID(self, id):
        if id in self.supported_parameters.keys():
            parameter = self.supported_parameters[id]
            response = self.connection.read_parameter(parameter)
            return parameter.get_value(response)
        else:
            return None

    def getParamListByID(self, ids):
        validParams = []
        for id in ids:
            if id in self.supported_parameters.keys():
                validParams.append(self.supported_parameters[id])
        if validParams:  # List not empty
            responses = self.connection.read_parameters(validParams)
            values = {}
            for i in range(len(responses)):
                values[validParams[i].get_id()] = validParams[i].get_value(responses[i])
            return values
        else:
            return None


    """####################################################
    Internal methods
    ####################################################"""


    def initConnection(self):
        """
        initConnection() - Parse teh parameter files and establish the serial connection to the ECU
        """

        #Initialize the connection
        init_finished = False

        while not init_finished:
            try:
                self._logFile.info('Trying to establish connection to ecu.')
                self.connection.open()
                #Query ecu/tcu to see which parameters are supported.
                ecu_packet = self.connection.init(1)
                tcu_packet = self.connection.init(2)

                if ecu_packet == None or tcu_packet == None:
                    print self._logFile.info('Cannot get initial data.')
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
                self._logFile.info('Connection initialized.')

            except IOError as e:
                print "I/O error: {0} {1}".format(e.errno, e.strerror)

                if self.connection != None:
                    self.connection.close()
                    time.sleep(3)
                continue

    def __initCoreParameters__(self):
        # read in core parameters from config file.
        pass

    def closeConnection(self):
        """
        closeConnection() - Closes the serial connection to the ECU
        """
        self.connection.close()

    def lookupParams(self, paramIds):
        """
        lookupParams(paramIds) - Looks up a given list of parameters in the master supported parameter list via the ID.
            paramIds - List of parameter Ids to look up.
        Return: Dictionary of parameters keyed by id.
        """
        params = {}
        for id in paramIds:
            for p in self.supported_parameters.keys():
                if p.get_id() == id:
                    params[id] = p
        return params
