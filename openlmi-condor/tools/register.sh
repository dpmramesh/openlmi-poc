#!/bin/sh

function usage()
{
    printf "Usage: $0 [ register | unregister ] mof reg\n"
}

function register()
{
    mof=$1
    reg=$2
    /usr/bin/sfcbstage -r $reg $mof
    /usr/bin/sfcbrepos -f
    /usr/bin/systemctl reload-or-try-restart sblim-sfcb.service
}

function unregister()
{
    mof=$1
    reg=$2
    /usr/bin/sfcbunstage -r $(basename $reg) $(basename $mof)
    /usr/bin/sfcbrepos -f
    /usr/bin/systemctl reload-or-try-restart sblim-sfcb.service
}

if [ $# -lt 3 ];
then
    usage
    exit 1
fi

case $1 in
    register)
        register $2 $3
        break;;
    unregister)
        unregister $2 $3
        break;;
    **)
        usage
        exit 1
esac
