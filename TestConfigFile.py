from Util.Config import *

"""
Test functionality of the config file reading/writing.
"""

parser = Config()
parser.setDefaultConfig()

parser.setMonitoredParams(["P1", "P36", "E3"])
parser.setRpmThresholds([200,400,66,234])

temp = parser.getMonitoredParams()
print temp

temp = parser.getRpmThresholds()
print temp