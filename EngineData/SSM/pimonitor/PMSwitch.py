'''
Feb 2016
@author: Adam Young
'''

import re


class PMSwitch(object):


    def __init__(self, sid, name, desc, byte_index, bit_index, address, target):

        self._id = sid
        self._name = name
        self._desc = desc
        self._byte_index = byte_index
        self._bit_index = bit_index
        self._target = target
        self._parameters = []
        self._address = address


    def get_id(self):
		return self._id

    def set_address(self, address, length):
		self._address = address
		self._address_length = length

    def get_address(self):
		return self._address

    def get_address_length(self):
		return self._address_length

    def get_name(self):
		return self._name

    def add_parameter(self, parameter):
		self._parameters.append(parameter)

    def get_parameters(self):
		return self._parameters

    def get_value(self, packet):
        data_byte = packet.get_data()[1]
        return ((data_byte&(1<<self._bit_index))!=0);

    def is_supported(self, data):
		if self._byte_index != "none" and self._bit_index != "none" and len(data) > self._byte_index:
			cubyte = data[self._byte_index]
			bitmask = 1 << self._bit_index
			return cubyte & bitmask == bitmask
		else:
			return False

    def to_string(self):
		return "Param: id=" + self._id + ", name=" + self._name + ", desc=" + self._desc + ", byte=" + str(self._byte_index) + \
		", bit=" + str(self._bit_index) + ", target=" + str(self._target) + \
		", address=" + hex(self._address)