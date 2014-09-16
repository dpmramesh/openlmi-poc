#!/bin/bash

CURAJAR=../build/src/OpenLMICli.jar
SBLIMJAR=/usr/share/java/sblim-cim-client2.jar
ARGSJAR=/usr/share/java/args4j.jar

usage(){
	echo "Usage: $0 [OpenLMIPower|OpenLMIService|OpenLMIUser|OpenLMIStorage"
	exit 1
}

[[ $# -eq 0 ]] && usage

CLASS=$1
shift
cmd="java -cp ${SBLIMJAR}:${ARGSJAR}:${CURAJAR} org.openlmi.${CLASS,,}.$CLASS $@"
$cmd

