#!/usr/bin/python
#
# This simple CIM client invokes the Widget CIM Provider. In particular
# the add() method. 
#
# test_widget.py -> SFCB CIMON -> /usr/lib/cmpi/libcmpiWidget_Widget.so 
# 
# Author: Javi Roman <javiroman@kernel-labs.org>

import sys
import pywbem

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

insts  = cliconn.ExecQuery('WQL', 'select * from KC_Widget')

# The invocation of CIM method (an extrinsic method) with the following method parameters:
#
# string Method_Name - The name of the method that will be invoked.
# pywbem.CIMInstanceName Object_Name - A reference to a CIM instance. The InstanceName or 
#					ClassName of the object on which the method is invoked.
# 

ret = cliconn.InvokeMethod('Add', 
		insts[0].classname,
		bc=insts[0].path, 
		X=pywbem.Uint32(sys.argv[1]), 
		Y=pywbem.Uint32(sys.argv[2]))

print "result: %s" % ret[0]
print "error: %s" % ret[1]
