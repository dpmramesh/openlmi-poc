#!/usr/bin/python
# Copyright (C) 2012  Javi Roman <javiroman@kernel-labs.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
# This simple CIM client invokes the Widget CIM Provider. In particular
# the add() method. 
#
# test_widget.py -> SFCB CIMON -> /usr/lib/cmpi/libcmpiWidget_Widget.so 

import sys
import pywbem
import json

if len(sys.argv) < 3:
    print """Usage: %s operand-1 operand-2

Example: %s 10 20""" % (sys.argv[0], sys.argv[0])
    sys.exit(1)

url = "https://127.0.0.1:5989"
username = None
password = None

# The first thing to do for any CIM transaction is to open a PyWBEM connection. 
# A connection is represented as an instance of a WBEMConnection class.
# The first parameter to WBEMConnection is a URL to the CIM Server. 
# The second parameter is a two-tuple containing the username and password. 
# The URL will probably start with "http", or "https". 
# Or, you can also supply an absolute path to a Unix Domain Socket:
# cliconn = pywbem.WBEMConnection('/var/run/tog-pegasus/cimxml.socket')

cliconn = pywbem.WBEMConnection(url, (username, password))
cliconn.debug = True

# The ExecQuery operations executes a query against target namespace:
#
# ExecQuery <objec>.ExecQuery([IN] string QueryyLanguage, [IN]string Query)
#
# The QueryLanguage input parameter defines the query language in which the query parameter
# is expressed. CIM and WBEM support a query mechanism that is used to select sets of
# properties from CIM object instances. The CIM Server (CIMON) implements a Query Engine
# to parse the query and evalute its results. The CIM Query Language used in the queries
# is based on concepts of SQL-92, and W3C XML Query.
# The CIM Query Language (CQL) is specified in "CIM Operations over HTTP Specification - DSP0200".
# The support of queries with the semantics Select-From-Where is called WQL - WBEM Query Language.

#insts  = cliconn.ExecQuery('WQL', 'select * from LMI_BasicExecutionServiceCondorFactory')
insts = cliconn.EnumerateInstanceNames("LMI_BasicExecutionServiceCondorFactory")

dictionary = {}
for i in insts:
	for ii in range(len(i.items())):
		key, value = i.items()[ii]
		dictionary[str(key)] = str(value)
	print dictionary["Name"]

# select the instance for working on. The target condor_schedd for
# running the Job.
instance = cliconn.GetInstance(insts[0])
#print instance

Job = {"Universe" : "vanilla",
"Executable" : "/bin/sleep",
"Arguments" : 30,
"Log" : "simple.log",
"Output" : "simple.out",
"Error" : "simple.error",
"Queue" : 150}

try:
    ret = cliconn.InvokeMethod('CreateActivity', 
			instance.classname,
			Request=json.dumps(Job))

except pywbem.CIMError, arg:
    if arg[0] != pywbem.CIM_ERR_NOT_SUPPORTED:
        print 'InvokeMethod(instancename): %s' % arg[1]
        sys.exit(1)

print "result code: %s" % ret[0]
print "result values (Job id): %s" % ret[1]
