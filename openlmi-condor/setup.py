from distutils.core import setup
setup(
    name='openlmi-condor',
    description='Condor Batch Scheduler Provider',
    author='Javi Roman',
    author_email='javiroman@kernel-labs.org',
    url='https://github.com/javiroman/openlmi-poc/tree/master/openlmi-condor',
    version='0.1',
    package_dir={'openlmi.storage': 'providers'},
    packages=['openlmi.storage', 'openlmi.storage.wrapper', 'openlmi.storage.util'],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: POSIX :: Linux',
        'Topic :: System :: Systems Administration',
        ]
    )
