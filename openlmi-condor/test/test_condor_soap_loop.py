#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# We need the following in order to use Condor SOAP:
# 1. yum install python-suds 
# 2. yum install condor (in order to get *.wsdl schemas).
#    For codor 7.8.x. For condor 7.9.x
# 3. Enable the SOAP interface in the central manager machine
# with the minimal entries in condor_config.local:
# - Turn on SOAP functionality
# ENABLE_SOAP = TRUE
#
# - Enable the web-service
# ENABLE_WEB_SERVER = TRUE
# WEB_ROOT_DIR=$(RELEASE_DIR)/web
#
# - Give everyone access... yikes! (you should probably not allow for 
# this in a production environment)
# ALLOW_SOAP = */*
# QUEUE_ALL_USERS_TRUSTED = TRUE
#
# - Set a well known port for the schedd to listen on
# SCHEDD_ARGS = -p 8080
# OSTALLOW_WRITE = *

from suds.client import Client
import logging
import sys

CONDOR_HOST      = "mncars002"
SCHEDD_PORT      = "8080"
COLLEC_PORT      = "9618"
SCHEDD_LOCATION  = "http://" + CONDOR_HOST + ":" + SCHEDD_PORT
COLLEC_LOCATION  = "http://" + CONDOR_HOST + ":" + COLLEC_PORT
WSDL_SCHEDD_FILE = "file:condorSchedd.wsdl"
WSDL_COLLEC_FILE = "file:condorCollector.wsdl"

#
# Logging
#
#logging.basicConfig(level=logging.INFO)
#logging.getLogger('suds.client').setLevel(logging.DEBUG)

def updateAdProperty(job, name, type=None, value=None):
    for i in range(len(job[1][0])):
        if (job[1][0][i].name == name):
            if type:
                job[1][0][i].type = type
            if value:
                job[1][0][i].value = value
            return True
    return False

def classad_dict(ad):
    native = {}
    attrs = ad[0]
    for attr in attrs:
        native[attr['name']] = attr['value']
    return native

#
# We can query to any queue scheduler
#
condor_schedd = Client(WSDL_SCHEDD_FILE, location=SCHEDD_LOCATION)
ads = condor_schedd.service.getJobAds(None, None)

cache = condor_schedd.options.cache
cache.setduration(seconds=200)
#print ads

#
# We can query to the pool collector
#
condor_collector = Client(WSDL_COLLEC_FILE, location=COLLEC_LOCATION)
vers = condor_collector.service.getVersionString()
print vers

schedds = condor_collector.service.queryScheddAds()
#print schedds

#
# Print methods availabe in the SOAP Client
#
#print condor_schedd

print "BasicExecutionServiceCondorFactory instances (condor_schedd):"
for i in range(len(schedds[0])):
	schedd_ad = classad_dict(schedds[0][i])
	print schedd_ad["Machine"] + " -> " + schedd_ad["ScheddIpAddr"]

# 
# Job submission cycle:
# 1. beginTransaction.
# 2. newCluster
# 3. newJob
# 4. createJobTemplate
# 5. submit
# 6. commitTransaction
#
transaction = condor_schedd.service.beginTransaction(10);
transactionId = transaction[1]
print "TransactionId: %s" % transactionId

cluster = condor_schedd.service.newCluster(transactionId)
clusterId=cluster[1]
print "ClusterId: %s" % clusterId

print "createJobTemplate"
job_template = condor_schedd.service.createJobTemplate(clusterId, 0, "condor", 5, "/bin/sleep", "30", "")

for i in xrange(int(sys.argv[1])):
	print "newJob for clusterId: %s" % clusterId
	job = condor_schedd.service.newJob(transactionId, clusterId)
	jobId = job[1]
	print "updating template"
	updateAdProperty(job_template, "ProcId", value=jobId)
	updateAdProperty(job_template, "LeaveJobInQueue", value="FALSE")
	jobAd = job_template[1]
	print "submit jobId -> %s" % jobId
	result = condor_schedd.service.submit(transactionId, clusterId, jobId, jobAd)

result = condor_schedd.service.commitTransaction(transactionId)
condor_schedd.service.requestReschedule();
#res = condor_schedd.service.closeSpool(transaction, clusterId, jobId)
print result

# vim: ts=4:et:sw=4:tw=80:sts=4:cc=80
