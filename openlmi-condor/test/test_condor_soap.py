#!/usr/bin/env python
#
# Minimal entries in condor_config.local
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

SUBMISSION_MACHINE = "mncars002"
SCHEDD_SOAP_PORT   = "8080"
SCHEDD_LOCATION    = "http://" + SUBMISSION_MACHINE + ":" + SCHEDD_SOAP_PORT=

condor_schedd = Client("file:///usr/lib64/condor/webservice/condorSchedd.wsdl", location=SCHEDD_LOCATION)
ads = condor_schedd.service.getJobAds(None, None)
print ads
