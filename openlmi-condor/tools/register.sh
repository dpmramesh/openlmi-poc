#!/bin/sh

PROVIDER_REPO="/usr/lib/python2.7/site-packages/openlmi/condor/"

function usage()
{
    printf "Usage: $0 [ register | unregister ] mof reg provider\n"
}

function register()
{
    mof=$1
    reg=$2
    /usr/bin/sfcbstage -r $reg $mof
    /usr/bin/sfcbrepos -f
    #/usr/bin/systemctl reload-or-try-restart sblim-sfcb.service

    cp -i $4 $PROVIDER_REPO
}

function unregister()
{
    mof=$1
    reg=$2
    /usr/bin/sfcbunstage -r $(basename $reg) $(basename $mof)
    /usr/bin/sfcbrepos -f
    #/usr/bin/systemctl reload-or-try-restart sblim-sfcb.service

    rm -i ${PROVIDER_REPO}/$4
}

if [ $# -lt 4 ];
then
    usage
    exit 1
fi

CIM_VERSION=$(readlink /usr/share/mof/cim-current/CIM_Schema.mof | cut -d'_' -f3)
echo "CIM v${CIM_VERSION%.mof}"

exit
case $1 in
    register)
        register $2 $3 $4
        break;;
    unregister)
        unregister $2 $3 $4
        break;;
    **)
        usage
        exit 1
esac
