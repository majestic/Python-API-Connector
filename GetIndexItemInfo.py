
# Version 0.9.3
# 
# Copyright (c) 2011, Majestic-12 Ltd
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#   1. Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#   2. Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#   3. Neither the name of the Majestic-12 Ltd nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.
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

# NOTE: The code below is specifically for the GetIndexItemInfo API command
#       For other API commands, the arguments required may differ.
#       Please refer to the Majestic SEO Developer Wiki for more information
#       regarding other API commands and their arguments.

from majesticseo_external_rpc.APIService import *
    
if(__name__ == '__main__'):
    endpoint = 'http://enterprise.majesticseo.com/api_command'

    print ('\n***********************************************************'
            + '*****************')

    print ('\nEndpoint: ' + endpoint)

    if('http://enterprise.majesticseo.com/api_command' == endpoint):
        print ('\nThis program is hard-wired to the Enterprise API.')
        
        print ('\nIf you do not have access to the Enterprise API, '
            + 'change the endpoint to: \nhttp://developer.majesticseo.com/api_command.')
    else:
        print ('\nThis program is hard-wired to the Developer API '
            + 'and hence the subset of data \nreturned will be substantially '
            + 'smaller than that which will be returned from \neither the '
            + 'Enterprise API or the Majestic SEO website.')

        print ('\nTo make this program use the Enterprise API, change '
            + 'the endpoint to: \nhttp://enterprise.majesticseo.com/api_command.')

    print ('\n***********************************************************'
                    + '*****************')

    print ('\n\nThis example program will return key information about \'index items\'.'
            + '\n\nThe following must be provided in order to run this program: '
            + '\n1. API key \n2. List of items to query')

    app_api_key = raw_input('\nPlease enter your API key:\n')

    print ('\nPlease enter the list of items you wish to query seperated by commas: '
            + '\n(e.g. majesticseo.com, majestic12.co.uk)')

    items_to_query = raw_input()
    items = items_to_query.split(', ')

    # create a hash from the resulting array with the key being
    # 'item0 => first item to query, item1 => second item to query' etc
    parameters = {}
    for index, item in enumerate(items):
        parameters['item' + str(index)] = item
        
    # add the total number of items to the hash with the key being 'items'
    parameters['items'] = len(items)

    parameters['datasource'] = 'fresh'

    api_service = APIService(app_api_key, endpoint)
    response = api_service.execute_command('GetIndexItemInfo', parameters)

    # check the response code
    if(response.is_ok()):
        # print the results table
        results = response.get_table_for_name('Results')
        for row in results.rows:
            item = row['Item']
            print '\n<' + str(item) + '>'
            for key in sorted(row.keys()):
                if('Item' != key):
                    value = row[key]
                    print ' ' + str(key) + ' ... ' + str(value)

        if('http://developer.majesticseo.com/api_command' == endpoint):
            print ('\n\n***********************************************************'
                + '*****************')

            print ('\nEndpoint: ' + endpoint)

            print ('\nThis program is hard-wired to the Developer API '
                + 'and hence the subset of data \nreturned will be substantially '
                + 'smaller than that which will be returned from \neither the '
                + 'Enterprise API or the Majestic SEO website.')

            print ('\nTo make this program use the Enterprise API, change '
                + 'the endpoint to: \nhttp://enterprise.majesticseo.com/api_command.')

            print ('\n***********************************************************'
                + '*****************')
    else:
        print ('\nERROR MESSAGE:')
        print (str(response.get_error_message()))

        print ('\n\n***********************************************************'
            + '*****************')

        print ('\nDebugging Info:')
        print ('\n  Endpoint: \t' + endpoint)
        print ('  API Key: \t' + app_api_key)

        if('http://enterprise.majesticseo.com/api_command' == endpoint):
            print ('\n  Is this API Key valid for this Endpoint?')

            print ('\n  This program is hard-wired to the Enterprise API.')

            print ('\n  If you do not have access to the Enterprise API, '
                + 'change the endpoint to: \n  http://developer.majesticseo.com/api_command.')

        print ('\n***********************************************************'
                    + '*****************')