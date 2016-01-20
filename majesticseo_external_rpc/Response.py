
# Copyright 2015, Majestic-12 Ltd trading as Majestic
# https://majestic.com
# 
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
# 
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
# 
#     * Neither the name of Majestic-12 Ltd, its trademarks, nor any contributors
#       to the software may be used to endorse or promote products derived from
#       this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL Majestic-12 Ltd BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import DataTable
from DataTable import *
from xml.sax import handler
from xml.sax import make_parser

class Response:
    
    """ 
    This constructs a new instance of the Response module. 
    The 'code' and 'error_message' parameters will default to None if not provided. 
    """
    def __init__(self, response, code = None, error_message = None):
        self.attributes = {}
        self.params = {}
        self.tables = {}
        if(None != response):
            handler = Handler(self)
            parser = make_parser()
            parser.setContentHandler(handler)
            #print response.read()
            parser.parse(response)  
        if(None != code and None != error_message):
            self.attributes['Code'] = code
            self.attributes['ErrorMessage'] = error_message
            self.attributes['FullError'] = error_message
    
    """ Indicates whether the response is ok """
    def is_ok(self):
        return self.get_code() in {'OK', 'QueuedForProcessing'};
    
    """ 
    Returns the Response's message code - 'OK' represents predicted state, all else represents an error. 
    """
    def get_code(self):
        return self.attributes['Code']
    
    """ Returns the error message(if present) from the Response """
    def get_error_message(self):
        return self.attributes['ErrorMessage']
    
    """ Returns the full error message(if present) from the Response """
    def get_full_error(self):
        return self.attributes['FullError']
    
    """ Returns a specific parameter from the Response's parameters """
    def get_param_for_name(self, name):
        if(name in self.params):
            return self.params[name]
        return None        
    
    """ Returns a specific DataTable object from the Response's data tables """
    def get_table_for_name(self, name):
        if(name in self.tables):
            return self.tables[name]
        return DataTable()
   
        
class Handler(handler.ContentHandler):
    
    """ Constructs a SAX handler for Majestic SEO's API data """
    def __init__(self, response):
        self.response = response
        self.data_table = None
        self.is_row = False
        self.row = ''
        
    """ Parses the start element """
    def startElement(self, name, attrs): 
        if(name == 'Result'):
            for attr_name in attrs.getNames():  
                self.response.attributes[attr_name] = attrs.getValue(attr_name)
        if(name == 'GlobalVars'):
            for attr_name in attrs.getNames():
                self.response.params[attr_name] = attrs.getValue(attr_name)
        if(name == 'DataTable'):
            self.data_table = DataTable()
            self.data_table.set_table_name(attrs.getValue('Name'))  
            self.data_table.set_table_headers(attrs.getValue('Headers'))
            for attr_name in attrs.getNames():
                if('Name' != attr_name and 'Headers' != attr_name):
                    self.data_table.set_table_params(attr_name, attrs.getValue(attr_name))
            self.response.tables[self.data_table.name] = self.data_table
        if(name == 'Row'):
            self.is_row = True
       
    """ Parses the data within the elements """
    def characters(self, chrs):
        if(self.is_row): 
            self.row += chrs
      
    """ Parses the end element """
    def endElement(self, name):
        if('Row' == name):
            self.data_table.set_table_row(self.row)
            self.is_row = False
            self.row = ''