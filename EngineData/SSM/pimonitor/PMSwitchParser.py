__author__ = 'Adam'

'''
Created on 29-03-2013

@author: citan
'''

import xml.sax
import os.path

from EngineData.SSM.pimonitor import PMSwitch


# TODO: dependencies
# TODO: ecuparams

class PMSwitchParser(xml.sax.ContentHandler):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        xml.sax.ContentHandler.__init__(self)

    def parse(self, file_name):
        self._switches = set()
        self._switch = None
        self._element_no = 0

        self._message = "Parsing XML data"
        source = open(os.path.join("../SSM/data", file_name))
        xml.sax.parse(source, self)

        return self._switches

    """
    Override to make sure we parse the romraider xml properly
    """
    def startElement(self, name, attrs):
        if name == "switch":
            # set optional arguments
            byte_index = "none"
            bit_index = "none"

            for (k,v) in attrs.items():
                if k == "id":
                    sid = v
                if k == "name":
                    name = v
                if k == "desc":
                    desc = v
                if k == "ecubyteindex":
                    byte_index = int(v)
                if k == "ecubit":
                    bit_index = int(v)
                if k == "target":
                    target = int(v)
                if k == "byte":
                    address = int(v, 16)
            self._switch = PMSwitch(sid, name, desc, byte_index, bit_index, address, target)



    """
    Override to make sure we parse the romraider xml properly
    """
    def endElement(self, name):
        if name == "switch":
            self._switches.add(self._switch)
            self._switch = None

        self._element_no += 1

