'''
Created on 29-03-2013

@author: citan

Feb. 2016 - Updated by Adam Young to allow it to also parse extended ecu parameters.

'''

import xml.sax
import os.path

from EngineData.SSM.pimonitor.PMParameter import PMParameter


# TODO: dependencies
# TODO: ecuparams

class PMXmlParser(xml.sax.ContentHandler):
    '''
    classdocs
    '''


    def __init__(self, ecuid):
        '''
        Constructor
        '''
        xml.sax.ContentHandler.__init__(self)
        self._ecuid = ecuid

    def parse(self, file_name):
        self._parameters = set()
        self._parameter = None
        self._element_no = 0
        self._inExtended = False
        self._extendedMatch = False

        self._message = "Parsing XML data"

        source = open(os.path.join("./EngineData/SSM/pimonitor/", file_name))

        xml.sax.parse(source, self)

        return self._parameters

    """
    Override to make sure we parse the romraider xml properly
    """
    def startElement(self, name, attrs):
        if name == "parameter" or name == "ecuparam":
            # set optional arguments
            byte_index = "none"
            bit_index = "none"

            # check for extended ecu parameter
            if name == "ecuparam":
                self._inExtended = True

            for (k,v) in attrs.items():
                if k == "id":
                    pid = v
                if k == "name":
                    param_name = v
                if k == "desc":
                    desc = v
                if k == "ecubyteindex":
                    byte_index = int(v)
                if k == "ecubit":
                    bit_index = int(v)
                if k == "target":
                    target = int(v)

            self._parameter = PMParameter(pid, param_name, desc, byte_index, bit_index, target)

        if name == "ecu":
            for (k,v) in attrs.items():
                if k == "id":
                    if v == self._ecuid:
                        self._extendedMatch = True;

        if name == "address":
            self._addrlen = 1
            for (k,v) in attrs.items():
                if k == "length":
                    self._addrlen = int(v)

        if name == "depends":
            self._addrlen = 0

        if name == "ref":
            for (k,v) in attrs.items():
                if k == "parameter":
                    self._parameter.add_dependency(v)

        if name == "conversion" and self._parameter != None:
            for (k,v) in attrs.items():
                if k == "units":
                    units = v
                if k == "expr":
                    expr = v
                if k == "format":
                    value_format = v

            if self._parameter != None:
                self._parameter.add_conversion([units, expr, value_format])

        self._name = name

    """
    This is an overirde of the content handler class.  Needed to parse the rom raider xml file
    """
    def characters(self, content):
        if len(content.strip()) > 0 and self._name == "address" and self._parameter != None:
            if self._inExtended and self._extendedMatch:
                self._parameter.set_address(int(content, 16), self._addrlen)
                self._extendedMatch = False
            else:
                self._parameter.set_address(int(content, 16), self._addrlen)


    """
    Override to make sure we parse the romraider xml properly
    """
    def endElement(self, name):
        if name == "parameter":
            self._parameters.add(self._parameter)
            self._parameter = None
            self._addrlen = None

        if name == "ecuparam" and self._parameter.get_address() != 0:
            self._parameters.add(self._parameter)
            self._parameter = None
            self._addrlen = None
            self._inExtended = False
            self._extendedMatch = False

        if name == "address":
            self._addrlen = 0

        if name == "depends":
            pass

        self._name = ""

        self._element_no += 1

