#!/bin/bash

CURAJAR=../build/src/CuraCli.jar
SBLIMJAR=/usr/share/java/sblim-cim-client2.jar

usage(){
	echo "Usage: $0 [CuraPower|CuraService|CuraUser" 
	exit 1
}

[[ $# -eq 0 ]] && usage

cmd="java -cp ${SBLIMJAR}:${CURAJAR} org.curacli.$1"
echo $cmd; $cmd

