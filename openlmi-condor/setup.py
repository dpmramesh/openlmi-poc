#!/usr/bin/env python

from distutils.core import setup
setup(
    name='openlmi-condor',
    version='0.1',
    description='Condor Batch Scheduler Provider',
    author='Javi Roman',
    author_email='javiroman@kernel-labs.org',
    url='https://github.com/javiroman/openlmi-poc/tree/master/openlmi-condor',
    package_dir={'openlmi.condor':'providers'},
    packages=['openlmi.condor'],
    classifiers=[
	'Development Status :: 1 - Alpha',
	'Environment :: Console',
	'Environment :: Web WBEM Environment',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: POSIX :: Linux',
        'Topic :: System :: Systems Administration',
	'Programming Language :: Python',
	'Intended Audience :: Developers',
	'Intended Audience :: System Administrators',
       ]
)
