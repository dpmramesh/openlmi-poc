- These examples were tested in Fedora 17 distro.

- Two CIMON tested:
	Pegasus : Package name "tog-pegasus"
	SFCB: Package name "sblim-sfcb"

- Package requeriments:
	"cim-schema"
	"cmpi-bindings-pywbem"

- We use a CIM browser YAWN that uses PyWBEM and runs
under Apache and mod_python module. Package name: "yawn"

A simple sample using SFCB as CIMON:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

$ su -c "yum install cim-schema sblim-sfcb cmpi-bindings-pywbem yawn"
$ su -c "systemctl start httpd.service"
$ su -c "systemctl start sblim-sfcb.service"
	
We can use yawn in http://localhost/yawn in order to browse the CIM
providers herarchy, but I'm unable to login this tool. I've to disable
the autentication with /etc/sfcb/sfcb.cfg -> doBasicAuth: false

1. We've created a new CIM class as a subclass of CIM_UnixProcess with
the MOF file Py_UnixProcess.mof. 

2. The second step is compile the MOF file into the CIMON repository.

3. In this example we use SFCB as CIMON, the tools available for the
compilation are: sfcbstage, and sfcbrepos.

4. sfcbstage - Script to copy provider MOF and registration files to the 
Small-Footprint CIM Broker (sfcb) staging area. The staging area is
a system location: /var/lib/sfcb/stage/ so we have to run the following
command as root:

	fcbstage -n root/cimv2 Py_UnixProcess.mof

This command only copy the Py_UnixProcess.mof file in the folder
/var/lib/sfcb/stage/mofs/root/cimv2/. The SFCB MOF compiler, invoked by sfcbstage,
automatically finds the missing schema elements, and imports them. In this case
Py_UnixProcess.mof is a derivated class of CIM_UnixProcess, so the file
/usr/share/sblim-cmpi-base/Linux_Base.mof (???) is imported in the stagin area too.

5. sfcbrepos - rebuilds  the  sfcb  class repository from the staging files. 
Rebuilding is done offline and the sfcb CIMOM must be restarted for changes 
to take effect.

	sfcbrepos -f

6. su -c "systemctl restart sblim-sfcb.service"

7. Using YAWM, the CIM object browser, we can see the following herarchy:

CIM_Management
    |
    `- CIM_ManagedSystemElement
        |
        `- CIM_LogicalElement
    	    |
    	    `- CIM_EnabledLogicalElement
    	        |
    	        `- CIM_Process
    	            |
    		    `- CIM_UnixProcess
    		       |
                       `- Py_UnixProcess



















