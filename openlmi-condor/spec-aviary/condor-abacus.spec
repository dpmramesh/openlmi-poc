%define tarball_version 7.8.6
Summary: HTCondor for Abacus: High Throughput Computing
Name: condor
Version: 7.8.6
Release: 0.1%{?dist}
Packager: Javi Roman <jroman@cediant.es>
Vendor: CEDIANTa HPC Business Solutions
License: ASL 2.0
Group: Applications/System
URL: http://www.cs.wisc.edu/condor/
# MD5Sum of upstream source:
#   76f596f6c69d482e451e940ce1221531  condor_src-7.8.6-all-all.tar.gz
Source0: condor_src-7.8.6-all-all.tar.gz
Patch0: condor_config.local.generic.patch
Patch1: condor_config.generic.patch

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: %_bindir/cmake
BuildRequires: %_bindir/flex
BuildRequires: %_bindir/byacc
BuildRequires: krb5-devel
BuildRequires: pcre-devel
BuildRequires: openssl-devel
BuildRequires: wso2-wsf-cpp-devel >= 2.1.0-4
BuildRequires: wso2-axis2-devel >= 2.1.0-4
BuildRequires: bind-utils
BuildRequires: libX11-devel
BuildRequires: libcom_err
BuildRequires: /usr/include/curl/curl.h
BuildRequires: /usr/include/expat.h

Requires: mailx
Requires: python >= 2.2
Requires(pre): shadow-utils
Requires(post):/sbin/chkconfig
Requires(post): policycoreutils
Requires(preun):/sbin/chkconfig
Requires(preun):/sbin/service
Requires(postun):/sbin/service

%description
Condor is a workload management system for high-throughput and
high-performance jobs. Like other full-featured batch systems, Condor
provides a job queueing mechanism, scheduling policy, priority scheme,
resource monitoring, and resource management. Users submit their
serial or parallel jobs to Condor, Condor places them into a queue,
chooses when and where to run the jobs based upon a policy, carefully
monitors their progress, and ultimately informs the user upon
completion.

%package aviary
Summary: Condor Aviary components
Group: Applications/System
Requires: %name = %version-%release
Requires: python-suds >= 0.4.1

%description aviary
Components to provide simplified WS interface to Condor.

%pre
getent group condor >/dev/null || groupadd -g 64 -r condor
getent passwd condor >/dev/null || \
  useradd -u 64 -r -g condor -d %_var/lib/condor -s /sbin/nologin \
    -c "Owner of Condor Daemons" condor
exit 0

%prep
%setup -q -n %name-%{tarball_version}

echo "Applying %{PATCH0}"
patch -p1 -f -s < %{PATCH0} || :

echo "Applying %{PATCH1}"
patch -p1 -f -s < %{PATCH1} || :

%build
%cmake -DCMAKE_INSTALL_PREFIX:PATH=%{buildroot}/%{_usr} \
       -DBUILDID:STRING=abacus-%{version}-%{release} \
       -DWITH_GSOAP:BOOL=FALSE \
       -DWITH_MANAGEMENT:BOOL=TRUE \
       -DWANT_FULL_DEPLOYMENT:BOOL=FALSE \
       -D_VERBOSE:BOOL=TRUE \
       -DWANT_CONTRIB:BOOL=TRUE \
       
make 

%install
# installation happens into a temporary location, this function is
# useful in moving files into their final locations
function populate {
  _dest="$1"; shift; _src="$*"
  mkdir -p "%{buildroot}/$_dest"
  mv $_src "%{buildroot}/$_dest"
}

# this function will copy, instead of move, files to their final locations
function populate_cp {
  _dest="$1"; shift; _src="$*"
  mkdir -p "%{buildroot}/$_dest"
  cp -r $_src "%{buildroot}/$_dest"
}

rm -rf %{buildroot}
make install

#
# Here customizations after condor intall
#

# The install target puts etc/ under usr/, let's fix that.
mv %{buildroot}/%{_usr}/etc %{buildroot}/%{_sysconfdir}

populate %_sysconfdir/condor %{buildroot}/%{_usr}/lib/condor_ssh_to_job_sshd_config_template

# Things in /usr/lib really belong in /usr/share/condor
populate %{_datadir}/condor %{buildroot}/%{_usr}/lib/*
# Except for libclassad
populate %{_libdir}/ %{buildroot}/%{_datadir}/condor/libclassad.so*

populate %{_libdir}/condor/plugins %{buildroot}/%{_usr}/libexec/*-plugin.so

# It is proper to put Condor specific libexec binaries under libexec/condor/
populate %{_libexecdir}/condor %{buildroot}/%{_usr}/libexec/*

# move to lib64 location
populate %{_libdir}/ %{buildroot}/%{_datadir}/condor/libcondor_utils*.so
populate %{_libdir}/ %{buildroot}/%{_datadir}/condor/libcondorapi.*

# man pages go under %{_mandir}
mkdir -p %{buildroot}/%{_mandir}
mv %{buildroot}/%{_usr}/man/man1 %{buildroot}/%{_mandir}

mkdir -p %{buildroot}/%{_sysconfdir}/condor
# the default condor_config file is not architecture aware and thus
# sets the LIB directory to always be /usr/lib, we want to do better
# than that. this is, so far, the best place to do this
# specialization. we strip the "lib" or "lib64" part from _libdir and
# stick it in the LIB variable in the config.
LIB=$(echo %{?_libdir} | sed -e 's:/usr/\(.*\):\1:')
if [ "$LIB" = "%_libdir" ]; then
  echo "_libdir does not contain /usr, sed expression needs attention"
  exit 1
fi
sed -e "s:^LIB\s*=.*:LIB = \$(RELEASE_DIR)/$LIB/condor:" \
  %{buildroot}/etc/examples/condor_config.generic \
  > %{buildroot}/%{_sysconfdir}/condor/condor_config

# Install the basic configuration, a Personal Condor config. Allows for
# yum install condor + service condor start and go.
mkdir -m0755 %{buildroot}/%{_sysconfdir}/condor/config.d
cp %{buildroot}/etc/examples/condor_config.local %{buildroot}/%{_sysconfdir}/condor/config.d/00personal_condor.config

# Install condor-qmf's base plugin configuration
populate %_sysconfdir/condor/config.d %{buildroot}/etc/examples/60condor-qmf.config
# Install condor-aviary's base plugin configuration
populate %_sysconfdir/condor/config.d %{buildroot}/etc/examples/61aviary.config

mkdir -p %{buildroot}/%{_var}/lib/condor/aviary
populate %{_var}/lib/condor/aviary %{buildroot}/usr/axis2.xml
populate %{_var}/lib/condor/aviary %{buildroot}/usr/services/

mkdir -p -m0755 %{buildroot}/%{_var}/run/condor
mkdir -p -m0755 %{buildroot}/%{_var}/log/condor
mkdir -p -m0755 %{buildroot}/%{_var}/lock/condor
mkdir -p -m1777 %{buildroot}/%{_var}/lock/condor/local
mkdir -p -m0755 %{buildroot}/%{_var}/lib/condor/spool
mkdir -p -m1777 %{buildroot}/%{_var}/lib/condor/execute

populate %{_datadir}/cluster %{buildroot}/etc/examples/condor.sh

rm %{buildroot}/%{_sbindir}/condor_set_shutdown
rm %{buildroot}/%{_mandir}/man1/condor_set_shutdown.1.gz

# not packaging glidein support, depends on globus
rm %{buildroot}/%{_mandir}/man1/condor_glidein.1.gz
rm %{buildroot}/%{_mandir}/man1/condor_config_bind.1.gz
rm %{buildroot}/%{_mandir}/man1/condor_cold_start.1.gz
rm %{buildroot}/%{_mandir}/man1/condor_cold_stop.1.gz
rm %{buildroot}/%{_mandir}/man1/uniq_pid_midwife.1.gz
rm %{buildroot}/%{_mandir}/man1/uniq_pid_undertaker.1.gz
rm %{buildroot}/%{_mandir}/man1/filelock_midwife.1.gz
rm %{buildroot}/%{_mandir}/man1/filelock_undertaker.1.gz
rm %{buildroot}/%{_mandir}/man1/install_release.1.gz
rm %{buildroot}/%{_mandir}/man1/cleanup_release.1.gz

# not packaging standard universe
rm %{buildroot}/%{_mandir}/man1/condor_compile.1.gz
rm %{buildroot}/%{_mandir}/man1/condor_checkpoint.1.gz

# not packaging configure/install scripts
rm %{buildroot}/%{_mandir}/man1/condor_configure.1.gz

# not packaging quill bits
rm %{buildroot}/%{_mandir}/man1/condor_load_history.1.gz

# Remove junk
rm -r %{buildroot}/%{_sysconfdir}/sysconfig
rm -r %{buildroot}/%{_sysconfdir}/init.d
rm -f %{buildroot}/%{_datadir}/condor/Condor.pm

# install the lsb init script
install -Dp -m0755 %{buildroot}/etc/examples/condor.init %{buildroot}/%{_initrddir}/condor

# we must place the config examples in builddir so %doc can find them
mv %{buildroot}/etc/examples %{_builddir}/%{name}-%{tarball_version}

# not packaging libraries from other packages
rm -f %{buildroot}/%{_datadir}/condor/condor/libcom_err.so.2
rm -f %{buildroot}/%{_datadir}/condor/condor/libcrypto.so.10
rm -f %{buildroot}/%{_datadir}/condor/condor/libexpat.so.1
rm -f %{buildroot}/%{_datadir}/condor/condor/libgssapi_krb5.so.2
rm -f %{buildroot}/%{_datadir}/condor/condor/libk5crypto.so.3
rm -f %{buildroot}/%{_datadir}/condor/condor/libkrb5.so.3
rm -f %{buildroot}/%{_datadir}/condor/condor/libkrb5support.so.0
rm -f %{buildroot}/%{_datadir}/condor/condor/liblber-2.4.so.2
rm -f %{buildroot}/%{_datadir}/condor/condor/libldap-2.4.so.2
rm -f %{buildroot}/%{_datadir}/condor/condor/libpcre.so.0
rm -f %{buildroot}/%{_datadir}/condor/condor/libssl.so.10
rm -f %{buildroot}/%{_datadir}/condor/condor/libssl3.so

%clean
rm -rf %{buildroot}

%check
# This currently takes hours and can kill your machine...
#cd condor_tests
#make check-seralized

%files
# qmf
%defattr(-,root,root,-)
%doc LICENSE-2.0.txt NOTICE.txt
%_sysconfdir/condor/config.d/60condor-qmf.config
%dir %_libdir/condor/plugins
%_libdir/condor/plugins/MgmtCollectorPlugin-plugin.so
%_libdir/condor/plugins/MgmtMasterPlugin-plugin.so
%_libdir/condor/plugins/MgmtNegotiatorPlugin-plugin.so
%_libdir/condor/plugins/MgmtScheddPlugin-plugin.so
%_libdir/condor/plugins/MgmtStartdPlugin-plugin.so

%_libdir/libcondor_utils_7_8_6.so
#%_libdir/libcondorapi.a
%_libdir/libcondorapi.so

%_bindir/get_trigger_data
%_sbindir/condor_trigger_config
%_sbindir/condor_triggerd
%_sbindir/condor_job_server

%_bindir/condor_drain
%_bindir/condor_glidein
%_bindir/condor_test_match

#%_includedir/MyString.h
#%_includedir/chirp_client.h
#%_includedir/compat_classad.h
#%_includedir/compat_classad_list.h
#%_includedir/compat_classad_util.h
#%_includedir/condor_classad.h
#%_includedir/condor_constants.h
#%_includedir/condor_event.h
#%_includedir/condor_header_features.h
#%_includedir/condor_holdcodes.h
#%_includedir/file_lock.h
#%_includedir/iso_dates.h
#%_includedir/read_user_log.h
#%_includedir/stl_string_utils.h
#%_includedir/user_log.README
#%_includedir/user_log.c++.h
#%_includedir/write_user_log.h

#%{_usr}/DOC
#%{_usr}/INSTALL
#%{_usr}/LICENSE-2.0.txt
#%{_usr}/README
#%{_usr}/src/chirp/chirp_client.c
#%{_usr}/src/chirp/chirp_client.h
#%{_usr}/src/chirp/chirp_protocol.h

%defattr(-,root,root,-)
%doc LICENSE-2.0.txt NOTICE.txt examples
%_initrddir/condor
%dir %_sysconfdir/condor/
%config %_sysconfdir/condor/condor_config
%dir %_sysconfdir/condor/config.d/
%_sysconfdir/condor/config.d/00personal_condor.config
%_sysconfdir/condor/condor_ssh_to_job_sshd_config_template
%dir %_datadir/condor/
%_datadir/condor/Chirp.jar
%_datadir/condor/CondorJavaInfo.class
%_datadir/condor/CondorJavaWrapper.class
%_datadir/condor/scimark2lib.jar
%_datadir/cluster/condor.sh
%_datadir/condor/CondorPersonal.pm
%_datadir/condor/CondorTest.pm
%_datadir/condor/CondorUtils.pm
%_datadir/condor/
#%_libdir/libchirp_client.a
%_datadir/condor/libchirp_client.so

#%dir %_datadir/condor/webservice/
#%_datadir/condor/webservice/condorCollector.wsdl
#%_datadir/condor/webservice/condorSchedd.wsdl

%dir %_libexecdir/condor/
%_libexecdir/condor/condor_chirp
%_libexecdir/condor/condor_job_router
%_libexecdir/condor/condor_ssh
%_libexecdir/condor/sshd.sh
%_libexecdir/condor/condor_limits_wrapper.sh
%_libexecdir/condor/condor_schedd.init
%_libexecdir/condor/condor_rooster
%_libexecdir/condor/condor_ssh_to_job_shell_setup
%_libexecdir/condor/condor_ssh_to_job_sshd_setup
%_libexecdir/condor/condor_kflops
%_libexecdir/condor/condor_mips
%_libexecdir/condor/data_plugin
%_libexecdir/condor/curl_plugin
%_libexecdir/condor/condor_shared_port
%_libexecdir/condor/accountant_log_fixer
%_libexecdir/condor/condor_defrag
%_libexecdir/condor/condor_glexec_cleanup
%_libexecdir/condor/condor_glexec_job_wrapper
%_libexecdir/condor/condor_glexec_kill
%_libexecdir/condor/condor_glexec_run
%_libexecdir/condor/condor_glexec_setup
%_libexecdir/condor/condor_glexec_update_proxy
%_libexecdir/condor/condor_glexec_wrapper
%_libexecdir/condor/condor_power_state
%_libexecdir/condor/glexec_starter_setup.sh
%_libexecdir/condor/libvirt_simple_script.awk

%_mandir/man1/condor_advertise.1.gz
%_mandir/man1/condor_config_val.1.gz
%_mandir/man1/condor_findhost.1.gz
%_mandir/man1/condor_history.1.gz
%_mandir/man1/condor_hold.1.gz
%_mandir/man1/condor_master.1.gz
%_mandir/man1/condor_off.1.gz
%_mandir/man1/condor_on.1.gz
%_mandir/man1/condor_preen.1.gz
%_mandir/man1/condor_prio.1.gz
%_mandir/man1/condor_procd.1.gz
%_mandir/man1/condor_q.1.gz
%_mandir/man1/condor_qedit.1.gz
%_mandir/man1/condor_reconfig.1.gz
%_mandir/man1/condor_release.1.gz
%_mandir/man1/condor_reschedule.1.gz
%_mandir/man1/condor_restart.1.gz
%_mandir/man1/condor_rm.1.gz
%_mandir/man1/condor_run.1.gz
%_mandir/man1/condor_stats.1.gz
%_mandir/man1/condor_status.1.gz
%_mandir/man1/condor_store_cred.1.gz
%_mandir/man1/condor_submit.1.gz
%_mandir/man1/condor_submit_dag.1.gz
%_mandir/man1/condor_updates_stats.1.gz
%_mandir/man1/condor_userlog.1.gz
%_mandir/man1/condor_userprio.1.gz
%_mandir/man1/condor_vacate.1.gz
%_mandir/man1/condor_vacate_job.1.gz
%_mandir/man1/condor_check_userlogs.1.gz
%_mandir/man1/condor_chirp.1.gz
%_mandir/man1/condor_cod.1.gz
%_mandir/man1/condor_dagman.1.gz
%_mandir/man1/condor_fetchlog.1.gz
%_mandir/man1/condor_transfer_data.1.gz
%_mandir/man1/condor_version.1.gz
%_mandir/man1/condor_wait.1.gz
%_mandir/man1/condor_power.1.gz
%_mandir/man1/condor_router_history.1.gz
%_mandir/man1/condor_continue.1.gz
%_mandir/man1/condor_suspend.1.gz
%_mandir/man1/condor_router_q.1.gz
%_mandir/man1/condor_gather_info.1.gz
%_mandir/man1/condor_router_rm.1.gz
%_mandir/man1/gidd_alloc.1.gz
%_mandir/man1/procd_ctl.1.gz
%_mandir/man1/condor_ssh_to_job.1.gz

%_bindir/condor_submit_dag
%_bindir/condor_prio
%_bindir/condor_transfer_data
%_bindir/condor_check_userlogs
%_bindir/condor_q
%_libexecdir/condor/condor_transferer
%_bindir/condor_cod
%_bindir/condor_qedit
%_bindir/condor_userlog
%_bindir/condor_release
%_bindir/condor_userlog_job_counter
%_bindir/condor_config_val
%_bindir/condor_reschedule
%_bindir/condor_userprio
%_bindir/condor_dagman
%_bindir/condor_rm
%_bindir/condor_vacate
%_bindir/condor_router_history
%_bindir/condor_router_q
%_bindir/condor_router_rm
%_bindir/condor_run
%_bindir/condor_vacate_job
%_bindir/condor_findhost
%_bindir/condor_stats
%_bindir/condor_version
%_bindir/condor_history
%_bindir/condor_status
%_bindir/condor_wait
%_bindir/condor_hold
%_bindir/condor_submit
%_bindir/condor_ssh_to_job
%_bindir/condor_power
%_bindir/condor_gather_info
%_bindir/condor_continue
%_bindir/condor_suspend
%_sbindir/ec2_gahp
%_sbindir/condor_advertise
%_sbindir/condor_c-gahp
%_sbindir/condor_c-gahp_worker_thread
%_sbindir/condor_collector
%_sbindir/condor_fetchlog
%_sbindir/condor_gridmanager
%_sbindir/condor_had
%_sbindir/condor_init
%_sbindir/condor_master
%_sbindir/condor_negotiator
%_sbindir/condor_off
%_sbindir/condor_on
%_sbindir/condor_preen
%_sbindir/condor_procd
%_sbindir/condor_reconfig
%_sbindir/condor_replication
%_sbindir/condor_restart
%_sbindir/condor_root_switchboard
%_sbindir/condor_schedd
%_sbindir/condor_shadow
%_sbindir/condor_startd
%_sbindir/condor_starter
%_sbindir/condor_store_cred
%_sbindir/condor_transferd
%_sbindir/condor_updates_stats
#%_sbindir/condor_configure
#%_sbindir/condor_credd
%_sbindir/condor_gridshell
#%_sbindir/condor_install
%_sbindir/condor_kbdd
%_sbindir/condor_vm-gahp
#%_sbindir/condor_vm-gahp-vmware
#%_sbindir/condor_vm_vmware
#%_sbindir/condor_vm_vmware.pl
%_sbindir/gahp_server
#%_sbindir/gidd_alloc
%_sbindir/grid_monitor
%_sbindir/grid_monitor.sh
%_sbindir/nordugrid_gahp
#%_sbindir/procd_ctl
%_sbindir/remote_gahp

#%_sbindir/condor_credd
#%_sbindir/condor_hdfs
%defattr(-,condor,condor,-)
%dir %_var/lib/condor/
%dir %_var/lib/condor/execute/
%dir %_var/log/condor/
%dir %_var/lib/condor/spool/
%dir %_var/lock/condor/
%dir %_var/lock/condor/local
%dir %_var/run/condor/

%defattr(-,root,root,-)
%doc LICENSE-2.0.txt NOTICE.txt
%_libdir/libclassad.so.7.8.6

%defattr(-,root,root,-)
%doc LICENSE-2.0.txt NOTICE.txt
%_bindir/classad_functional_tester
%_bindir/classad_version
%_libdir/libclassad.so
%_libdir/libclassad.so.3
%_datadir/condor/libclassad.a
%dir %_includedir/classad/
%_includedir/classad/attrrefs.h
%_includedir/classad/cclassad.h
%_includedir/classad/classad_distribution.h
%_includedir/classad/classadErrno.h
%_includedir/classad/classad.h
%_includedir/classad/classadItor.h
%_includedir/classad/classad_stl.h
%_includedir/classad/collectionBase.h
%_includedir/classad/collection.h
%_includedir/classad/common.h
%_includedir/classad/debug.h
%_includedir/classad/exprList.h
%_includedir/classad/exprTree.h
%_includedir/classad/fnCall.h
%_includedir/classad/indexfile.h
%_includedir/classad/lexer.h
%_includedir/classad/lexerSource.h
%_includedir/classad/literals.h
%_includedir/classad/matchClassad.h
%_includedir/classad/operators.h
%_includedir/classad/query.h
%_includedir/classad/sink.h
%_includedir/classad/source.h
%_includedir/classad/transaction.h
%_includedir/classad/util.h
%_includedir/classad/value.h
%_includedir/classad/view.h
%_includedir/classad/xmlLexer.h
%_includedir/classad/xmlSink.h
%_includedir/classad/xmlSource.h

%files aviary
%defattr(-,root,root,-)
%doc LICENSE-2.0.txt NOTICE.txt
%_sysconfdir/condor/config.d/61aviary.config
%dir %_libdir/condor/plugins
%_libdir/condor/plugins/AviaryScheddPlugin-plugin.so
%_libdir/condor/plugins/AviaryLocatorPlugin-plugin.so
%_sbindir/aviary_query_server
%dir %_datadir/condor/aviary
%_datadir/condor/aviary/jobcontrol.py*
%_datadir/condor/aviary/jobquery.py*
%_datadir/condor/aviary/submissions.py*
%_datadir/condor/aviary/submit.py*
%_datadir/condor/aviary/setattr.py*
%_datadir/condor/aviary/jobinventory.py*
%dir %_datadir/condor/aviary/dag
%_datadir/condor/aviary/dag/diamond.dag
%_datadir/condor/aviary/dag/dag-submit.py*
%_datadir/condor/aviary/dag/job.sub
%dir %_datadir/condor/aviary/module
%_datadir/condor/aviary/module/aviary/util.py*
%_datadir/condor/aviary/module/aviary/https.py*
%_datadir/condor/aviary/module/aviary/__init__.py*
%_datadir/condor/aviary/README
%defattr(-,condor,condor,-)
%dir %_var/lib/condor/aviary
%_var/lib/condor/aviary/axis2.xml
%dir %_var/lib/condor/aviary/services
%dir %_var/lib/condor/aviary/services/job
%_var/lib/condor/aviary/services/job/libaviary_job_axis.so
%_var/lib/condor/aviary/services/job/services.xml
%_var/lib/condor/aviary/services/job/aviary-common.xsd
%_var/lib/condor/aviary/services/job/aviary-job.xsd
%_var/lib/condor/aviary/services/job/aviary-job.wsdl
%dir %_var/lib/condor/aviary/services/query
%_var/lib/condor/aviary/services/query/libaviary_query_axis.so
%_var/lib/condor/aviary/services/query/services.xml
%_var/lib/condor/aviary/services/query/aviary-common.xsd
%_var/lib/condor/aviary/services/query/aviary-query.xsd
%_var/lib/condor/aviary/services/query/aviary-query.wsdl
%_var/lib/condor/aviary/services/locator/aviary-common.xsd
%_var/lib/condor/aviary/services/locator/aviary-locator.wsdl
%_var/lib/condor/aviary/services/locator/aviary-locator.xsd
%_var/lib/condor/aviary/services/locator/libaviary_locator_axis.so
%_var/lib/condor/aviary/services/locator/services.xml
%_datadir/condor/aviary/locator.py
%_datadir/condor/aviary/locator.pyc
%_datadir/condor/aviary/locator.pyo
%_datadir/condor/aviary/submission_ids.py
%_datadir/condor/aviary/submission_ids.pyc
%_datadir/condor/aviary/submission_ids.pyo

%post -n condor
/sbin/chkconfig --add condor
/sbin/ldconfig
if [ -e /var/lib/condor/condor_master.pid ]; then
   mv /var/lib/condor/condor_master.pid /var/run/condor/condor_master.pid
fi

%preun -n condor
if [ $1 = 0 ]; then
  /sbin/service condor stop >/dev/null 2>&1 || :
  /sbin/chkconfig --del condor
fi

%postun -n condor
if [ "$1" -ge "1" ]; then
  /sbin/service condor condrestart >/dev/null 2>&1 || :
fi
/sbin/ldconfig

%changelog
* Thu Aug 30 2012 <tstclair@redhat> - 7.6.5-0.22
- Fix shadow errors (BZ852537)

