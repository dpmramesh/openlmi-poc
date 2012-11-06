#!/usr/bin/env python

from suds.client import Client
import logging

logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)

collector_url = 'http://somehost.example.com:9618/'

if __name__ == '__main__':
    url = '%scondorCollector.wsdl' % collector_url
    collector = Client(url, cache=None, location=collector_url)

    print collector.service.getVersionString()
