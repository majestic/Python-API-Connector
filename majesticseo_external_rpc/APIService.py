
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

import sys
import urllib
import urllib2
import Response
from Response import *

class APIService:
    
	""" 
	This constructs a new instance of the APIService module.
	'application_id' is the unique identifier for your application - for api requests, this is your "api key" ... for OpenApp request, this is your "private key".
	'endpoint' is required and must point to the url you wish to target; ie: enterprise or developer.
	E.g. api_service = ApiService.new('ABC123MYAPIKEY', 'https://developer.majestic.com/api_command'); 
	"""
	def __init__(self, application_id, end_point):
		self.application_id = application_id
		self.end_point = end_point

	""" 
	This method will execute the specified command as an api request.
	'name' is the name of the command you wish to execute, e.g. GetIndexItemInfo
	'parameters' is a hash containing the command parameters.
	'timeout' specifies the amount of time to wait before aborting the transaction. This defaults to 5 seconds. 
	"""
	def execute_command(self, name, parameters, timeout=5):
		parameters['app_api_key'] = self.application_id
		parameters['cmd'] = name
		return self.execute_request(parameters, timeout);


	""" 
	This will execute the specified command as an OpenApp request.
	'command_name' is the name of the command you wish to execute, e.g. GetIndexItemInfo
	'parameters' is a hash containing the command parameters.
	'access_token' the token provided by the user to access their resources.
	'timeout' specifies the amount of time to wait before aborting the transaction. This defaults to 5 seconds. 
	"""
	def execute_openapp_request(self, command_name, parameters, access_token, timeout=5):
		parameters['accesstoken'] = access_token
		parameters['cmd'] = command_name
		parameters['privatekey'] = self.application_id
		return self.execute_request(parameters, timeout);


	def execute_request(self, parameters, timeout):
		parameters = urllib.urlencode(parameters)
		request = urllib2.Request(self.end_point)
		response = urllib2.urlopen(request, parameters, timeout)
		
		try:
			return Response(response)
		except Exception:
			return Response(None, 'ConnectionError', sys.exc_info()[0])
		finally:
			response.close()


