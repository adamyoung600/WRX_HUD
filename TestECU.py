from EngineData.EcuData import EcuData

ecu = EcuData()

print "Test 1 - Get parameters via list"
testList = ['E25',  # Gear Selection
                       'S4',  # Neutral Switch
                       'S23',  # Clutch Switch
                       'P30',  # Pedal Angle
                       'E11',  # Feedback Knock Control
                       'E1',  # IAM
                       'P8']  # RPM
values = ecu._getParamListByID(testList)
print values

print "Test 2 - Set monitored parameters"
ecu.setMonitoredParams(testList)
print ecu._monitoredParamData

print "Test 3 - Update values"
ecu.refreshData(false)
print ecu._coreParamData
print ecu._monitoredParamData


print "Test 4 - Update values"
print ecu._logParamData(true)

