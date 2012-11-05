#!/usr/bin/env python

import pywbem
# This module (code-generation functionality) is not automatically loaded with an 'import pywbem', 
# so as to not load the module when only the pywbem client functionality is desired.
from pywbem.cim_provider2 import codegen

# establish a connection with the CIMOM 
con = pywbem.WBEMConnection('https://localhost')

# retrieve the CIM class object for PyTut_Foo from the root/cimv2 namespace
cc = con.GetClass('LMI_BasicExecutionServiceCondorFactory', 'root/cimv2')

# We now have all the information we need about the PyTut_Foo class stored in the
# cc variable. We can now as pywbem to generated the code for use. 
python_code, registration_mof = codegen(cc)

# The python_code variable should contain a stubbed out version of our provider,
# and the registration_mof should contain the MOF for our provider registration.i
# These will both need modification. 
codefile = open('LMI_BasicExecutionServiceCondorFactory.py', 'w')
codefile.write(python_code)
codefile.close()

regfile = open('LMI_BasicExecutionServiceCondorFactory.reg', 'w')
regfile.write(registration_mof)
regfile.close()

cc = con.GetClass('LMI_BasicExecutionServiceCondorManagement', 'root/cimv2')

# We now have all the information we need about the PyTut_Foo class stored in the
# cc variable. We can now as pywbem to generated the code for use. 
python_code, registration_mof = codegen(cc)

# The python_code variable should contain a stubbed out version of our provider,
# and the registration_mof should contain the MOF for our provider registration.i
# These will both need modification. 
codefile = open('LMI_BasicExecutionServiceCondorManagement.py', 'w')
codefile.write(python_code)
codefile.close()

regfile = open('LMI_BasicExecutionServiceCondorManagement.reg', 'w')
regfile.write(registration_mof)
regfile.close()
