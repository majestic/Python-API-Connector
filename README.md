Python-API-Connector (for Python 2.7.0)
====================

Majestic® surveys and maps the Internet and has created the largest commercial Link Intelligence database in the world. The Majestic® search engine is mainly used to instantly provide Flow Metrics® which evaluate the quality of any page on the Internet on a scale from 0 to 100. The connector libraries are supplied to assist in using the Majestic® API and are available in a number of programming languages.
 
Setup
---------------
Clone this repository in a directory. 

Set the PYTHONPATH environment variable to the Python-API-Connector directory.
This allows Python to find the library and import it from your project.

On Windows you can use the `set` command:
```
set PYTHONPATH=C:\project\lib\Python-API-Connector
```
On linux use the `export` command instead: 
```
export PYTHONPATH=/usr/project/lib/Python-API-Connector
```
Examples
-------------
There are a few examples of using the API-Connector in the following scripts:

* GetIndexItemInfo.py 
  * The GetIndexItemInfo command provides data on the number of backlinks to any web page or site, linking domains and the main topics for that page or website
* GetBackLinkData.py 
  * GetBacklinkData will return rows of data with information about all the pages linking to a given URL or domain
  
The follwoing code is from GetIndexItemInfo.py and shows how the API-Connector can be used:

```
api_service = APIService(app_api_key, endpoint)
response = api_service.execute_command('GetIndexItemInfo', parameters)
```

Further notes  
------------------
The Python Connector has been developed using Python 2.7.2.
To run the examples have python 2+ installed, then in terminal use ```python2 somefile.py```  
On your system the command might instead be ```py somefile.py```.



For further information see api documentation @ https://developer-support.majestic.com/


