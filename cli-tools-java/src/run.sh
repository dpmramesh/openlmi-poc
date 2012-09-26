#!/bin/bash

CURAJAR=../build/src/CuraCli.jar
SBLIMJAR=/usr/share/java/sblim-cim-client2.jar
ARGSJAR=/usr/share/java/args4j.jar

usage(){
	echo "Usage: $0 [CuraPower|CuraService|CuraUser" 
	exit 1
}

[[ $# -eq 0 ]] && usage

CLASS=$1
shift
cmd="java -cp ${SBLIMJAR}:${ARGSJAR}:${CURAJAR} org.cura.${CLASS,,}.$CLASS $@"
$cmd

