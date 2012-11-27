#!/usr/bin/env python
# -*- coding: utf-8 -*-

from suds import *
from suds.client import Client
from sys import exit, argv
import time, pwd, os, logging
from aviary.util import *

CONDOR_HOST      = "mncars002"
SCHEDD_PORT      = "9090"
SCHEDD_LOCATION  = "http://" + CONDOR_HOST + ":" + SCHEDD_PORT + "/services/job/submitJob"
WSDL_SCHEDD_FILE = \
"file:/home/sarnoso/HACK/openlmi-poc.git/openlmi-condor/test/test-aviary/wsdl/services/job/aviary-job.wsdl"


plugins = []

uid = "condor"

parser = build_basic_parser('Submit a sample job remotely via SOAP.', \
                            SCHEDD_LOCATION)
(opts,args) =  parser.parse_args()

client = create_suds_client(opts, WSDL_SCHEDD_FILE, plugins)
client.set_options(location=opts.url)

#print client

# add specific requirements here
req1 = client.factory.create("ns0:ResourceConstraint")
req1.type = 'OS'
req1.value = 'LINUX'
reqs = [ req1 ]

# add extra Condor-specific or custom job attributes here
extra1 = client.factory.create("ns0:Attribute")
extra1.name = 'ClusterId'
extra1.type = 'INTEGER-ATTR'
extra1.value = '100'
extras = [ extra1 ]

for i in xrange(int(sys.argv[1])):
    try:
	    result = client.service.submitJob( \
	    # the executable command
		    '/bin/sleep', \
	    # some arguments for the command
		    '30', \
	    # the submitter name
		    uid, \
	    # initial working directory wwhere job will execute
		    '/tmp', \
	    # an arbitrary string identifying the target submission group
		    'python_test_submit', \
	    # special resource requirements
		    reqs,	\
	    # additional attributes
		    extras
	    )
    except Exception, e:
	    print "invocation failed at: ", opts.url
	    print e
	    exit(1)	

if result.status.code != "OK":
	print result.status.code,"; ", result.status.text
	exit(1)

print opts.verbose and result or result.id.job

# vim: ts=4:et:sw=4:tw=80:sts=4:cc=80
