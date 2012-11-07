"""Python Provider for LMI_BasicExecutionServiceCondorFactory

Instruments the CIM class LMI_BasicExecutionServiceCondorFactory

"""

import pywbem
from pywbem.cim_provider2 import CIMProvider2
from suds.client import Client

class LMI_BasicExecutionServiceCondorFactory(CIMProvider2):
    """Instrument the CIM class LMI_BasicExecutionServiceCondorFactory 

    The basic execution service (BES)is a service to which clients can send
    requests to initiate, monitor, and manage computational activities and
    access information about the BES. A BasicExecutionService can act on
    one or more execution environments - modeled, profiled, and
    instantiated as a ComputerSystem. There is no requirement that a
    BasicExecutionService reside on the node of a ComputerSystem on which
    it acts. The associations ServiceAvailToElement and
    ServiceAffectsElement relate the BasicExecutionService to
    ComputerSystem. The association HostedDependency expresses the concept
    that an execution environment may be contained within another
    execution environment. For example, in a grid or
    distributed/virtualized environment the whole point for not explicitly
    stating which execution environment to use up front is to allow some
    client software, e.g. scheduler, orchestrator, provisioner,
    application, to determine where to place the activity (in which
    execution environment) based on the input activity document (that
    activity\'s environment/resource requirements).

    In partircular for Condor batch scheduler, LMI_BESCondorFactory
    represents the machines with job submission capabilities. In a Condor
    pool these machines have condor_schedd daemons running. We will have
    an instance of this class per condor_schedd daemon in the Condor pool.
    
    """

    def __init__ (self, env):
        logger = env.get_logger()
        logger.log_debug('Initializing provider %s from %s' \
                % (self.__class__.__name__, __file__))

    def get_instance(self, env, model):
        """Return an instance.

        Keyword arguments:
        env -- Provider Environment (pycimmb.ProviderEnvironment)
        model -- A template of the pywbem.CIMInstance to be returned.  The 
            key properties are set on this instance to correspond to the 
            instanceName that was requested.  The properties of the model
            are already filtered according to the PropertyList from the 
            request.  Only properties present in the model need to be
            given values.  If you prefer, you can set all of the 
            values, and the instance will be filtered for you. 

        Possible Errors:
        CIM_ERR_ACCESS_DENIED
        CIM_ERR_INVALID_PARAMETER (including missing, duplicate, unrecognized 
            or otherwise incorrect parameters)
        CIM_ERR_NOT_FOUND (the CIM Class does exist, but the requested CIM 
            Instance does not exist in the specified namespace)
        CIM_ERR_FAILED (some other unspecified error occurred)

        """
        
        logger = env.get_logger()
        logger.log_debug('Entering %s.get_instance()' \
                % self.__class__.__name__)
        

        # TODO fetch system resource matching the following keys:
        #   model['CPUArchitecture']
        #   model['SystemName']
        #   model['TotalNumberOfContainedResources']
        #   model['OperatingSystem']
        #   model['IsAcceptingNewActivities']
        #   model['LocalResourceManagerType']
        #   model['LongDescription']
        #   model['CPUSpeed']
        #   model['SystemCreationClassName']
        #   model['CommonName']
        #   model['TotalNumberOfActivities']
        #   model['BESExtension']
        #   model['CPUCount']
        #   model['NamingProfile']
        #   model['ActivityReference']
        #   model['CreationClassName']
        #   model['VirtualMemory']
        #   model['PhysicalMemory']
        #   model['Name']

        #model['AvailableRequestedStates'] = [self.Values.AvailableRequestedStates.<VAL>,] # TODO 
        #model['Caption'] = '' # TODO 
        #model['CommunicationStatus'] = self.Values.CommunicationStatus.<VAL> # TODO 
        #model['Description'] = '' # TODO 
        #model['DetailedStatus'] = self.Values.DetailedStatus.<VAL> # TODO 
        #model['ElementName'] = '' # TODO 
        #model['EnabledDefault'] = self.Values.EnabledDefault.Enabled # TODO 
        #model['EnabledState'] = self.Values.EnabledState.Not_Applicable # TODO 
        #model['Generation'] = pywbem.Uint64() # TODO 
        #model['HealthState'] = self.Values.HealthState.<VAL> # TODO 
        #model['InstallDate'] = pywbem.CIMDateTime() # TODO 
        #model['InstanceID'] = '' # TODO 
        #model['OperatingStatus'] = self.Values.OperatingStatus.<VAL> # TODO 
        #model['OperationalStatus'] = [self.Values.OperationalStatus.<VAL>,] # TODO 
        #model['OtherEnabledState'] = '' # TODO 
        #model['PrimaryOwnerContact'] = '' # TODO 
        #model['PrimaryOwnerName'] = '' # TODO 
        #model['PrimaryStatus'] = self.Values.PrimaryStatus.<VAL> # TODO 
        #model['RequestedState'] = self.Values.RequestedState.Not_Applicable # TODO 
        #model['Started'] = bool() # TODO 
        #model['StartMode'] = self.Values.StartMode.<VAL> # TODO 
        #model['Status'] = self.Values.Status.<VAL> # TODO 
        #model['StatusDescriptions'] = ['',] # TODO 
        #model['TimeOfLastStateChange'] = pywbem.CIMDateTime() # TODO 
        #model['TransitioningToState'] = self.Values.TransitioningToState.Not_Applicable # TODO 
        return model

    def enum_instances(self, env, model, keys_only):
        """Enumerate instances.

        The WBEM operations EnumerateInstances and EnumerateInstanceNames
        are both mapped to this method. 
        This method is a python generator

        Keyword arguments:
        env -- Provider Environment (pycimmb.ProviderEnvironment)
        model -- A template of the pywbem.CIMInstances to be generated.  
            The properties of the model are already filtered according to 
            the PropertyList from the request.  Only properties present in 
            the model need to be given values.  If you prefer, you can 
            always set all of the values, and the instance will be filtered 
            for you. 
        keys_only -- A boolean.  True if only the key properties should be
            set on the generated instances.

        Possible Errors:
        CIM_ERR_FAILED (some other unspecified error occurred)

        """

        logger = env.get_logger()
        logger.log_debug('Entering %s.enum_instances()' \
                % self.__class__.__name__)
                
        # Prime model.path with knowledge of the keys, so key values on
        # the CIMInstanceName (model.path) will automatically be set when
        # we set property values on the model. 
        model.path.update({'IsAcceptingNewActivities': None,
            'LocalResourceManagerType': None, 'ActivityReference': None,
            'PhysicalMemory': None, 'Name': None, 'VirtualMemory': None,
            'CPUArchitecture': None, 'CPUSpeed': None, 'CommonName': None,
            'TotalNumberOfActivities': None, 'LongDescription': None,
            'BESExtension': None, 'CPUCount': None, 'SystemName': None,
            'NamingProfile': None, 'TotalNumberOfContainedResources':
            None, 'CreationClassName': None, 'OperatingSystem': None,
            'SystemCreationClassName': None})

        CONDOR_HOST      = "mncars002"
        SCHEDD_PORT      = "8080"
        COLLEC_PORT      = "9618"
        SCHEDD_LOCATION  = "http://" + CONDOR_HOST + ":" + SCHEDD_PORT
        COLLEC_LOCATION  = "http://" + CONDOR_HOST + ":" + COLLEC_PORT
        WSDL_SCHEDD_FILE = "file:condorSchedd.wsdl"
        WSDL_COLLEC_FILE = "file:/usr/lib/python2.7/site-packages/openlmi/condor/condorCollector.wsdl"
    
        condor_collector = Client(WSDL_COLLEC_FILE, location=COLLEC_LOCATION)
        schedds = condor_collector.service.queryScheddAds()

        instances = []
        for i in range(len(schedds[0])):
            schedd_ad = self._classad_dict(schedds[0][i])
            instances.append(schedd_ad["Machine"])

        for i in instances:
            # Key properties    
            model['CPUArchitecture'] = 'Intel Core5' 
            model['SystemName'] = 'Linux Host'
            model['TotalNumberOfContainedResources'] = '' 
            model['OperatingSystem'] = '' 
            model['IsAcceptingNewActivities'] = '1'
            model['LocalResourceManagerType'] = '' 
            model['LongDescription'] = '' 
            model['CPUSpeed'] = '' 
            model['SystemCreationClassName'] = ''
            model['CommonName'] = ''
            model['TotalNumberOfActivities'] = ''
            model['BESExtension'] = ''
            model['CPUCount'] = ''
            model['NamingProfile'] = ''
            model['ActivityReference'] = ''
            model['CreationClassName'] = 'LMI_BasicExecutionServiceCondorFactory'    
            model['VirtualMemory'] = ''
            model['PhysicalMemory'] = ''
            model['Name'] = i
            if keys_only:
                yield model
            else:
                try:
                    yield self.get_instance(env, model)
                except pywbem.CIMError, (num, msg):
                    if num not in (pywbem.CIM_ERR_NOT_FOUND, 
                                   pywbem.CIM_ERR_ACCESS_DENIED):
                        raise

    def set_instance(self, env, instance, modify_existing):
        """Return a newly created or modified instance.

        Keyword arguments:
        env -- Provider Environment (pycimmb.ProviderEnvironment)
        instance -- The new pywbem.CIMInstance.  If modifying an existing 
            instance, the properties on this instance have been filtered by 
            the PropertyList from the request.
        modify_existing -- True if ModifyInstance, False if CreateInstance

        Return the new instance.  The keys must be set on the new instance. 

        Possible Errors:
        CIM_ERR_ACCESS_DENIED
        CIM_ERR_NOT_SUPPORTED
        CIM_ERR_INVALID_PARAMETER (including missing, duplicate, unrecognized 
            or otherwise incorrect parameters)
        CIM_ERR_ALREADY_EXISTS (the CIM Instance already exists -- only 
            valid if modify_existing is False, indicating that the operation
            was CreateInstance)
        CIM_ERR_NOT_FOUND (the CIM Instance does not exist -- only valid 
            if modify_existing is True, indicating that the operation
            was ModifyInstance)
        CIM_ERR_FAILED (some other unspecified error occurred)

        """

        logger = env.get_logger()
        logger.log_debug('Entering %s.set_instance()' \
                % self.__class__.__name__)
        # TODO create or modify the instance
        raise pywbem.CIMError(pywbem.CIM_ERR_NOT_SUPPORTED) # Remove to implement
        return instance

    def delete_instance(self, env, instance_name):
        """Delete an instance.

        Keyword arguments:
        env -- Provider Environment (pycimmb.ProviderEnvironment)
        instance_name -- A pywbem.CIMInstanceName specifying the instance 
            to delete.

        Possible Errors:
        CIM_ERR_ACCESS_DENIED
        CIM_ERR_NOT_SUPPORTED
        CIM_ERR_INVALID_NAMESPACE
        CIM_ERR_INVALID_PARAMETER (including missing, duplicate, unrecognized 
            or otherwise incorrect parameters)
        CIM_ERR_INVALID_CLASS (the CIM Class does not exist in the specified 
            namespace)
        CIM_ERR_NOT_FOUND (the CIM Class does exist, but the requested CIM 
            Instance does not exist in the specified namespace)
        CIM_ERR_FAILED (some other unspecified error occurred)

        """ 

        logger = env.get_logger()
        logger.log_debug('Entering %s.delete_instance()' \
                % self.__class__.__name__)

        # TODO delete the resource
        raise pywbem.CIMError(pywbem.CIM_ERR_NOT_SUPPORTED) # Remove to implement

    def _classad_dict(self, ad):
        native = {}
        attrs = ad[0]
        for attr in attrs:
            native[attr['name']] = attr['value']
        return native


    def cim_method_requeststatechange(self, env, object_name,
                                      param_requestedstate=None,
                                      param_timeoutperiod=None):
        """Implements LMI_BasicExecutionServiceCondorFactory.RequestStateChange()

        Requests that the state of the element be changed to the value
        specified in the RequestedState parameter. When the requested
        state change takes place, the EnabledState and RequestedState of
        the element will be the same. Invoking the RequestStateChange
        method multiple times could result in earlier requests being
        overwritten or lost. \nA return code of 0 shall indicate the state
        change was successfully initiated. \nA return code of 3 shall
        indicate that the state transition cannot complete within the
        interval specified by the TimeoutPeriod parameter. \nA return code
        of 4096 (0x1000) shall indicate the state change was successfully
        initiated, a ConcreteJob has been created, and its reference
        returned in the output parameter Job. Any other return code
        indicates an error condition.
        
        Keyword arguments:
        env -- Provider Environment (pycimmb.ProviderEnvironment)
        object_name -- A pywbem.CIMInstanceName or pywbem.CIMCLassName 
            specifying the object on which the method RequestStateChange() 
            should be invoked.
        param_requestedstate --  The input parameter RequestedState (type pywbem.Uint16 self.Values.RequestStateChange.RequestedState) 
            The state requested for the element. This information will be
            placed into the RequestedState property of the instance if the
            return code of the RequestStateChange method is 0 (\'Completed
            with No Error\'), or 4096 (0x1000) (\'Job Started\'). Refer to
            the description of the EnabledState and RequestedState
            properties for the detailed explanations of the RequestedState
            values.
            
        param_timeoutperiod --  The input parameter TimeoutPeriod (type pywbem.CIMDateTime) 
            A timeout period that specifies the maximum amount of time that
            the client expects the transition to the new state to take.
            The interval format must be used to specify the TimeoutPeriod.
            A value of 0 or a null parameter indicates that the client has
            no time requirements for the transition. \nIf this property
            does not contain 0 or null and the implementation does not
            support this parameter, a return code of \'Use Of Timeout
            Parameter Not Supported\' shall be returned.
            

        Returns a two-tuple containing the return value (type pywbem.Uint32 self.Values.RequestStateChange)
        and a list of CIMParameter objects representing the output parameters

        Output parameters:
        Job -- (type REF (pywbem.CIMInstanceName(classname='CIM_ConcreteJob', ...)) 
            May contain a reference to the ConcreteJob created to track the
            state transition initiated by the method invocation.
            

        Possible Errors:
        CIM_ERR_ACCESS_DENIED
        CIM_ERR_INVALID_PARAMETER (including missing, duplicate, 
            unrecognized or otherwise incorrect parameters)
        CIM_ERR_NOT_FOUND (the target CIM Class or instance does not 
            exist in the specified namespace)
        CIM_ERR_METHOD_NOT_AVAILABLE (the CIM Server is unable to honor 
            the invocation request)
        CIM_ERR_FAILED (some other unspecified error occurred)

        """

        logger = env.get_logger()
        logger.log_debug('Entering %s.cim_method_requeststatechange()' \
                % self.__class__.__name__)

        # TODO do something
        raise pywbem.CIMError(pywbem.CIM_ERR_METHOD_NOT_AVAILABLE) # Remove to implemented
        out_params = []
        #out_params+= [pywbem.CIMParameter('job', type='reference', 
        #                   value=pywbem.CIMInstanceName(classname='CIM_ConcreteJob', ...))] # TODO
        #rval = # TODO (type pywbem.Uint32 self.Values.RequestStateChange)
        return (rval, out_params)
        
    def cim_method_stopservice(self, env, object_name):
        """Implements LMI_BasicExecutionServiceCondorFactory.StopService()

        The StopService method places the Service in the stopped state.
        Note that the function of this method overlaps with the
        RequestedState property. RequestedState was added to the model to
        maintain a record (such as a persisted value) of the last state
        request. Invoking the StopService method should set the
        RequestedState property appropriately. The method returns an
        integer value of 0 if the Service was successfully stopped, 1 if
        the request is not supported, and any other number to indicate an
        error. In a subclass, the set of possible return codes could be
        specified using a ValueMap qualifier on the method. The strings to
        which the ValueMap contents are translated can also be specified
        in the subclass as a Values array qualifier. \n\nNote: The
        semantics of this method overlap with the RequestStateChange
        method that is inherited from EnabledLogicalElement. This method
        is maintained because it has been widely implemented, and its
        simple "stop" semantics are convenient to use.
        
        Keyword arguments:
        env -- Provider Environment (pycimmb.ProviderEnvironment)
        object_name -- A pywbem.CIMInstanceName or pywbem.CIMCLassName 
            specifying the object on which the method StopService() 
            should be invoked.

        Returns a two-tuple containing the return value (type pywbem.Uint32)
        and a list of CIMParameter objects representing the output parameters

        Output parameters: none

        Possible Errors:
        CIM_ERR_ACCESS_DENIED
        CIM_ERR_INVALID_PARAMETER (including missing, duplicate, 
            unrecognized or otherwise incorrect parameters)
        CIM_ERR_NOT_FOUND (the target CIM Class or instance does not 
            exist in the specified namespace)
        CIM_ERR_METHOD_NOT_AVAILABLE (the CIM Server is unable to honor 
            the invocation request)
        CIM_ERR_FAILED (some other unspecified error occurred)

        """

        logger = env.get_logger()
        logger.log_debug('Entering %s.cim_method_stopservice()' \
                % self.__class__.__name__)

        # TODO do something
        raise pywbem.CIMError(pywbem.CIM_ERR_METHOD_NOT_AVAILABLE) # Remove to implemented
        out_params = []
        #rval = # TODO (type pywbem.Uint32)
        return (rval, out_params)
        
    def cim_method_changeaffectedelementsassignedsequence(self, env, object_name,
                                                          param_managedelements,
                                                          param_assignedsequence):
        """Implements LMI_BasicExecutionServiceCondorFactory.ChangeAffectedElementsAssignedSequence()

        This method is called to change relative sequence in which order
        the ManagedElements associated to the Service through
        CIM_ServiceAffectsElement association are affected. In the case
        when the Service represents an interface for client to execute
        extrinsic methods and when it is used for grouping of the managed
        elements that could be affected, the ordering represents the
        relevant priority of the affected managed elements with respect to
        each other. \nAn ordered array of ManagedElement instances is
        passed to this method, where each ManagedElement instance shall be
        already be associated with this Service instance via
        CIM_ServiceAffectsElement association. If one of the
        ManagedElements is not associated to the Service through
        CIM_ServiceAffectsElement association, the implementation shall
        return a value of 2 ("Error Occured"). \nUpon successful execution
        of this method, if the AssignedSequence parameter is NULL, the
        value of the AssignedSequence property on each instance of
        CIM_ServiceAffectsElement shall be updated such that the values of
        AssignedSequence properties shall be monotonically increasing in
        correlation with the position of the referenced ManagedElement
        instance in the ManagedElements input parameter. That is, the
        first position in the array shall have the lowest value for
        AssignedSequence. The second position shall have the second lowest
        value, and so on. Upon successful execution, if the
        AssignedSequence parameter is not NULL, the value of the
        AssignedSequence property of each instance of
        CIM_ServiceAffectsElement referencing the ManagedElement instance
        in the ManagedElements array shall be assigned the value of the
        corresponding index of the AssignedSequence parameter array. For
        ManagedElements instances which are associated with the Service
        instance via CIM_ServiceAffectsElement and are not present in the
        ManagedElements parameter array, the AssignedSequence property on
        the CIM_ServiceAffects association shall be assigned a value of 0.
        
        Keyword arguments:
        env -- Provider Environment (pycimmb.ProviderEnvironment)
        object_name -- A pywbem.CIMInstanceName or pywbem.CIMCLassName 
            specifying the object on which the method ChangeAffectedElementsAssignedSequence() 
            should be invoked.
        param_managedelements --  The input parameter ManagedElements (type REF (pywbem.CIMInstanceName(classname='CIM_ManagedElement', ...)) (Required)
            An array of ManagedElements.
            
        param_assignedsequence --  The input parameter AssignedSequence (type [pywbem.Uint16,]) (Required)
            An array of integers representing AssignedSequence for the
            ManagedElement in the corresponding index of the
            ManagedElements parameter.
            

        Returns a two-tuple containing the return value (type pywbem.Uint32 self.Values.ChangeAffectedElementsAssignedSequence)
        and a list of CIMParameter objects representing the output parameters

        Output parameters:
        Job -- (type REF (pywbem.CIMInstanceName(classname='CIM_ConcreteJob', ...)) 
            Reference to the job spawned if the operation continues after
            the method returns. (May be null if the task is completed).
            

        Possible Errors:
        CIM_ERR_ACCESS_DENIED
        CIM_ERR_INVALID_PARAMETER (including missing, duplicate, 
            unrecognized or otherwise incorrect parameters)
        CIM_ERR_NOT_FOUND (the target CIM Class or instance does not 
            exist in the specified namespace)
        CIM_ERR_METHOD_NOT_AVAILABLE (the CIM Server is unable to honor 
            the invocation request)
        CIM_ERR_FAILED (some other unspecified error occurred)

        """

        logger = env.get_logger()
        logger.log_debug('Entering %s.cim_method_changeaffectedelementsassignedsequence()' \
                % self.__class__.__name__)

        # TODO do something
        raise pywbem.CIMError(pywbem.CIM_ERR_METHOD_NOT_AVAILABLE) # Remove to implemented
        out_params = []
        #out_params+= [pywbem.CIMParameter('job', type='reference', 
        #                   value=pywbem.CIMInstanceName(classname='CIM_ConcreteJob', ...))] # TODO
        #rval = # TODO (type pywbem.Uint32 self.Values.ChangeAffectedElementsAssignedSequence)
        return (rval, out_params)
        
    def cim_method_terminateactivity(self, env, object_name,
                                     param_identifier=None):
        """Implements LMI_BasicExecutionServiceCondorFactory.TerminateActivity()

        This operation requests that one or more items in an execution
        environment be terminated. For example, within the context of the
        OGSA Basic Execution Services, this means that a new or existing
        activity in the container can be requested to be terminated, and
        the operation maps to the TerminateActivities() interface. The
        return value should be 0 if the request was successfully executed
        and some other value if an error occurred. The return code Invalid
        Request Message refers to the input of an invalid identifier.
        
        Keyword arguments:
        env -- Provider Environment (pycimmb.ProviderEnvironment)
        object_name -- A pywbem.CIMInstanceName or pywbem.CIMCLassName 
            specifying the object on which the method TerminateActivity() 
            should be invoked.
        param_identifier --  The input parameter Identifier (type [unicode,]) 
            Identifies one or more items in an execution environment that
            are to be terminated.
            

        Returns a two-tuple containing the return value (type pywbem.Uint32 self.Values.TerminateActivity)
        and a list of CIMParameter objects representing the output parameters

        Output parameters:
        Job -- (type REF (pywbem.CIMInstanceName(classname='CIM_ConcreteJob', ...)) 
            Reference to the job (can be null if the task is completed).
            
        Response -- (type [bool,]) 
            Boolean response value for each requested termination. A value
            of TRUE indicates successful termination.
            

        Possible Errors:
        CIM_ERR_ACCESS_DENIED
        CIM_ERR_INVALID_PARAMETER (including missing, duplicate, 
            unrecognized or otherwise incorrect parameters)
        CIM_ERR_NOT_FOUND (the target CIM Class or instance does not 
            exist in the specified namespace)
        CIM_ERR_METHOD_NOT_AVAILABLE (the CIM Server is unable to honor 
            the invocation request)
        CIM_ERR_FAILED (some other unspecified error occurred)

        """

        logger = env.get_logger()
        logger.log_debug('Entering %s.cim_method_terminateactivity()' \
                % self.__class__.__name__)

        # TODO do something
        raise pywbem.CIMError(pywbem.CIM_ERR_METHOD_NOT_AVAILABLE) # Remove to implemented
        out_params = []
        #out_params+= [pywbem.CIMParameter('job', type='reference', 
        #                   value=pywbem.CIMInstanceName(classname='CIM_ConcreteJob', ...))] # TODO
        #out_params+= [pywbem.CIMParameter('response', type='boolean', 
        #                   value=[bool(),])] # TODO
        #rval = # TODO (type pywbem.Uint32 self.Values.TerminateActivity)
        return (rval, out_params)
        
    def cim_method_getactivitystatus(self, env, object_name,
                                     param_identifier=None):
        """Implements LMI_BasicExecutionServiceCondorFactory.GetActivityStatus()

        This operation requests the status of one or more items in an
        execution environment. For example, within the context of the OGSA
        Basic Execution Services, this means that the status of one or
        more activities within an execution environment can be obtained,
        and the operation maps to the GetActivityStatuses() interface. The
        return value should be 0 if the request was successfully executed
        and some other value if an error occurred. The return code Invalid
        Request Message refers to the input of an invalid identifier.
        
        Keyword arguments:
        env -- Provider Environment (pycimmb.ProviderEnvironment)
        object_name -- A pywbem.CIMInstanceName or pywbem.CIMCLassName 
            specifying the object on which the method GetActivityStatus() 
            should be invoked.
        param_identifier --  The input parameter Identifier (type [unicode,]) 
            Identifies one or more items in an execution environment whose
            status will be obtained.
            

        Returns a two-tuple containing the return value (type pywbem.Uint32 self.Values.GetActivityStatus)
        and a list of CIMParameter objects representing the output parameters

        Output parameters:
        StatusResponse -- (type [unicode,]) 
            A response for each requested status.
            
        Job -- (type REF (pywbem.CIMInstanceName(classname='CIM_ConcreteJob', ...)) 
            Reference to the job (can be null if the task is completed).
            

        Possible Errors:
        CIM_ERR_ACCESS_DENIED
        CIM_ERR_INVALID_PARAMETER (including missing, duplicate, 
            unrecognized or otherwise incorrect parameters)
        CIM_ERR_NOT_FOUND (the target CIM Class or instance does not 
            exist in the specified namespace)
        CIM_ERR_METHOD_NOT_AVAILABLE (the CIM Server is unable to honor 
            the invocation request)
        CIM_ERR_FAILED (some other unspecified error occurred)

        """

        logger = env.get_logger()
        logger.log_debug('Entering %s.cim_method_getactivitystatus()' \
                % self.__class__.__name__)

        # TODO do something
        raise pywbem.CIMError(pywbem.CIM_ERR_METHOD_NOT_AVAILABLE) # Remove to implemented
        out_params = []
        #out_params+= [pywbem.CIMParameter('statusresponse', type='string', 
        #                   value=['',])] # TODO
        #out_params+= [pywbem.CIMParameter('job', type='reference', 
        #                   value=pywbem.CIMInstanceName(classname='CIM_ConcreteJob', ...))] # TODO
        #rval = # TODO (type pywbem.Uint32 self.Values.GetActivityStatus)
        return (rval, out_params)
        
    def cim_method_getattributesdocument(self, env, object_name):
        """Implements LMI_BasicExecutionServiceCondorFactory.GetAttributesDocument()

        This operation requests a document containing the basic execution
        service management attributes.The return code Invalid Request
        Message refers to the input of an invalid identifier.
        
        Keyword arguments:
        env -- Provider Environment (pycimmb.ProviderEnvironment)
        object_name -- A pywbem.CIMInstanceName or pywbem.CIMCLassName 
            specifying the object on which the method GetAttributesDocument() 
            should be invoked.

        Returns a two-tuple containing the return value (type pywbem.Uint32 self.Values.GetAttributesDocument)
        and a list of CIMParameter objects representing the output parameters

        Output parameters:
        AttrsDoc -- (type [unicode,]) 
            A XML document containing the various attributes within its
            associated container.
            
        Job -- (type REF (pywbem.CIMInstanceName(classname='CIM_ConcreteJob', ...)) 
            Reference to the job (can be null if the task is completed).
            

        Possible Errors:
        CIM_ERR_ACCESS_DENIED
        CIM_ERR_INVALID_PARAMETER (including missing, duplicate, 
            unrecognized or otherwise incorrect parameters)
        CIM_ERR_NOT_FOUND (the target CIM Class or instance does not 
            exist in the specified namespace)
        CIM_ERR_METHOD_NOT_AVAILABLE (the CIM Server is unable to honor 
            the invocation request)
        CIM_ERR_FAILED (some other unspecified error occurred)

        """

        logger = env.get_logger()
        logger.log_debug('Entering %s.cim_method_getattributesdocument()' \
                % self.__class__.__name__)

        # TODO do something
        raise pywbem.CIMError(pywbem.CIM_ERR_METHOD_NOT_AVAILABLE) # Remove to implemented
        out_params = []
        #out_params+= [pywbem.CIMParameter('attrsdoc', type='string', 
        #                   value=['',])] # TODO
        #out_params+= [pywbem.CIMParameter('job', type='reference', 
        #                   value=pywbem.CIMInstanceName(classname='CIM_ConcreteJob', ...))] # TODO
        #rval = # TODO (type pywbem.Uint32 self.Values.GetAttributesDocument)
        return (rval, out_params)
        
    def cim_method_startservice(self, env, object_name):
        """Implements LMI_BasicExecutionServiceCondorFactory.StartService()

        The StartService method places the Service in the started state.
        Note that the function of this method overlaps with the
        RequestedState property. RequestedState was added to the model to
        maintain a record (such as a persisted value) of the last state
        request. Invoking the StartService method should set the
        RequestedState property appropriately. The method returns an
        integer value of 0 if the Service was successfully started, 1 if
        the request is not supported, and any other number to indicate an
        error. In a subclass, the set of possible return codes could be
        specified using a ValueMap qualifier on the method. The strings to
        which the ValueMap contents are translated can also be specified
        in the subclass as a Values array qualifier. \n\nNote: The
        semantics of this method overlap with the RequestStateChange
        method that is inherited from EnabledLogicalElement. This method
        is maintained because it has been widely implemented, and its
        simple "start" semantics are convenient to use.
        
        Keyword arguments:
        env -- Provider Environment (pycimmb.ProviderEnvironment)
        object_name -- A pywbem.CIMInstanceName or pywbem.CIMCLassName 
            specifying the object on which the method StartService() 
            should be invoked.

        Returns a two-tuple containing the return value (type pywbem.Uint32)
        and a list of CIMParameter objects representing the output parameters

        Output parameters: none

        Possible Errors:
        CIM_ERR_ACCESS_DENIED
        CIM_ERR_INVALID_PARAMETER (including missing, duplicate, 
            unrecognized or otherwise incorrect parameters)
        CIM_ERR_NOT_FOUND (the target CIM Class or instance does not 
            exist in the specified namespace)
        CIM_ERR_METHOD_NOT_AVAILABLE (the CIM Server is unable to honor 
            the invocation request)
        CIM_ERR_FAILED (some other unspecified error occurred)

        """

        logger = env.get_logger()
        logger.log_debug('Entering %s.cim_method_startservice()' \
                % self.__class__.__name__)

        # TODO do something
        raise pywbem.CIMError(pywbem.CIM_ERR_METHOD_NOT_AVAILABLE) # Remove to implemented
        out_params = []
        #rval = # TODO (type pywbem.Uint32)
        return (rval, out_params)
        
    def cim_method_createactivity(self, env, object_name,
                                  param_request=None):
        """Implements LMI_BasicExecutionServiceCondorFactory.CreateActivity()

        This operation adds requests to the execution environment. For
        example, within the context of the OGSA Basic Execution Services,
        this means that a new activity is added to an execution
        environment, and the operation maps to the CreateActivity()
        interface. CreateActivity establishes the \'binding\' between the
        activity and the execution environment that will contain it.
        Selection / implementation of how an execution environment is
        outside the scope of basic execution service. In a grid or
        distributed environment, this allows other clients, e.g.
        schedulers, orchestrators, applications, to make decisions on
        which execution environment to select (place activity) based on
        the JSDL job description (the input activity document that
        describes that activity\'s environment/resource requirements. The
        return value should be 0 if the request was successfully executed
        and some other value if an error occurred. The output the
        CreateActivity method is an identifier which is used as input to
        other methods in this class to identify the activity being acted
        upon.
        
        Keyword arguments:
        env -- Provider Environment (pycimmb.ProviderEnvironment)
        object_name -- A pywbem.CIMInstanceName or pywbem.CIMCLassName 
            specifying the object on which the method CreateActivity() 
            should be invoked.
        param_request --  The input parameter Request (type unicode) 
            Describes a single request that is to be executed by an
            execution environment.
            

        Returns a two-tuple containing the return value (type pywbem.Uint32 self.Values.CreateActivity)
        and a list of CIMParameter objects representing the output parameters

        Output parameters:
        Job -- (type REF (pywbem.CIMInstanceName(classname='CIM_ConcreteJob', ...)) 
            Reference to the job (can be null if the task is completed).
            
        Identifier -- (type unicode) 
            Identifier associated with the requested execution. This
            Identifier is used as input to other Basic Execution service
            methods.
            

        Possible Errors:
        CIM_ERR_ACCESS_DENIED
        CIM_ERR_INVALID_PARAMETER (including missing, duplicate, 
            unrecognized or otherwise incorrect parameters)
        CIM_ERR_NOT_FOUND (the target CIM Class or instance does not 
            exist in the specified namespace)
        CIM_ERR_METHOD_NOT_AVAILABLE (the CIM Server is unable to honor 
            the invocation request)
        CIM_ERR_FAILED (some other unspecified error occurred)

        """

        logger = env.get_logger()
        logger.log_debug('Entering %s.cim_method_createactivity()' \
                % self.__class__.__name__)
       
        out_params = []
        #out_params+= [pywbem.CIMParameter('job', type='reference', 
        #                   value=pywbem.CIMInstanceName(classname='CIM_ConcreteJob', ...))] 
        out_params+= [pywbem.CIMParameter('Identifier', type='string', 
                           value='Este seria el job identifier')]
        print param_request
        rval = pywbem.Uint32(2) #pywbem.Uint32 # self.Values.CreateActivity
        return (rval, out_params)
        
    def cim_method_getactivitydocuments(self, env, object_name,
                                        param_identifier=None):
        """Implements LMI_BasicExecutionServiceCondorFactory.GetActivityDocuments()

        This operation requests activity document descriptions for a set of
        specified set of activities. These activity documents may be
        different from those initially input in the CreateActivity
        operation since this service may alter its contents to reflect
        policy or process within the service. The return code Invalid
        Request Message refers to the input of an invalid identifier.
        
        Keyword arguments:
        env -- Provider Environment (pycimmb.ProviderEnvironment)
        object_name -- A pywbem.CIMInstanceName or pywbem.CIMCLassName 
            specifying the object on which the method GetActivityDocuments() 
            should be invoked.
        param_identifier --  The input parameter Identifier (type [unicode,]) 
            Identifies one or more activities for which activity documents
            are requested.
            

        Returns a two-tuple containing the return value (type pywbem.Uint32 self.Values.GetActivityDocuments)
        and a list of CIMParameter objects representing the output parameters

        Output parameters:
        Job -- (type REF (pywbem.CIMInstanceName(classname='CIM_ConcreteJob', ...)) 
            Reference to the job (can be null if the task is completed).
            
        Response -- (type [unicode,]) 
            An array of activity document response elements.
            

        Possible Errors:
        CIM_ERR_ACCESS_DENIED
        CIM_ERR_INVALID_PARAMETER (including missing, duplicate, 
            unrecognized or otherwise incorrect parameters)
        CIM_ERR_NOT_FOUND (the target CIM Class or instance does not 
            exist in the specified namespace)
        CIM_ERR_METHOD_NOT_AVAILABLE (the CIM Server is unable to honor 
            the invocation request)
        CIM_ERR_FAILED (some other unspecified error occurred)

        """

        logger = env.get_logger()
        logger.log_debug('Entering %s.cim_method_getactivitydocuments()' \
                % self.__class__.__name__)

        # TODO do something
        raise pywbem.CIMError(pywbem.CIM_ERR_METHOD_NOT_AVAILABLE) # Remove to implemented
        out_params = []
        #out_params+= [pywbem.CIMParameter('job', type='reference', 
        #                   value=pywbem.CIMInstanceName(classname='CIM_ConcreteJob', ...))] # TODO
        #out_params+= [pywbem.CIMParameter('response', type='string', 
        #                   value=['',])] # TODO
        #rval = # TODO (type pywbem.Uint32 self.Values.GetActivityDocuments)
        return (rval, out_params)
        
    class Values(object):
        class DetailedStatus(object):
            Not_Available = pywbem.Uint16(0)
            No_Additional_Information = pywbem.Uint16(1)
            Stressed = pywbem.Uint16(2)
            Predictive_Failure = pywbem.Uint16(3)
            Non_Recoverable_Error = pywbem.Uint16(4)
            Supporting_Entity_in_Error = pywbem.Uint16(5)
            # DMTF_Reserved = ..
            # Vendor_Reserved = 0x8000..

        class RequestedState(object):
            Unknown = pywbem.Uint16(0)
            Enabled = pywbem.Uint16(2)
            Disabled = pywbem.Uint16(3)
            Shut_Down = pywbem.Uint16(4)
            No_Change = pywbem.Uint16(5)
            Offline = pywbem.Uint16(6)
            Test = pywbem.Uint16(7)
            Deferred = pywbem.Uint16(8)
            Quiesce = pywbem.Uint16(9)
            Reboot = pywbem.Uint16(10)
            Reset = pywbem.Uint16(11)
            Not_Applicable = pywbem.Uint16(12)
            # DMTF_Reserved = ..
            # Vendor_Reserved = 32768..65535

        class HealthState(object):
            Unknown = pywbem.Uint16(0)
            OK = pywbem.Uint16(5)
            Degraded_Warning = pywbem.Uint16(10)
            Minor_failure = pywbem.Uint16(15)
            Major_failure = pywbem.Uint16(20)
            Critical_failure = pywbem.Uint16(25)
            Non_recoverable_error = pywbem.Uint16(30)
            # DMTF_Reserved = ..
            # Vendor_Specific = 32768..65535

        class ChangeAffectedElementsAssignedSequence(object):
            Completed_with_No_Error = pywbem.Uint32(0)
            Not_Supported = pywbem.Uint32(1)
            Error_Occured = pywbem.Uint32(2)
            Busy = pywbem.Uint32(3)
            Invalid_Reference = pywbem.Uint32(4)
            Invalid_Parameter = pywbem.Uint32(5)
            Access_Denied = pywbem.Uint32(6)
            # DMTF_Reserved = 7..32767
            # Vendor_Specified = 32768..65535

        class TransitioningToState(object):
            Unknown = pywbem.Uint16(0)
            Enabled = pywbem.Uint16(2)
            Disabled = pywbem.Uint16(3)
            Shut_Down = pywbem.Uint16(4)
            No_Change = pywbem.Uint16(5)
            Offline = pywbem.Uint16(6)
            Test = pywbem.Uint16(7)
            Defer = pywbem.Uint16(8)
            Quiesce = pywbem.Uint16(9)
            Reboot = pywbem.Uint16(10)
            Reset = pywbem.Uint16(11)
            Not_Applicable = pywbem.Uint16(12)
            # DMTF_Reserved = ..

        class EnabledDefault(object):
            Enabled = pywbem.Uint16(2)
            Disabled = pywbem.Uint16(3)
            Not_Applicable = pywbem.Uint16(5)
            Enabled_but_Offline = pywbem.Uint16(6)
            No_Default = pywbem.Uint16(7)
            Quiesce = pywbem.Uint16(9)
            # DMTF_Reserved = ..
            # Vendor_Reserved = 32768..65535

        class EnabledState(object):
            Unknown = pywbem.Uint16(0)
            Other = pywbem.Uint16(1)
            Enabled = pywbem.Uint16(2)
            Disabled = pywbem.Uint16(3)
            Shutting_Down = pywbem.Uint16(4)
            Not_Applicable = pywbem.Uint16(5)
            Enabled_but_Offline = pywbem.Uint16(6)
            In_Test = pywbem.Uint16(7)
            Deferred = pywbem.Uint16(8)
            Quiesce = pywbem.Uint16(9)
            Starting = pywbem.Uint16(10)
            # DMTF_Reserved = 11..32767
            # Vendor_Reserved = 32768..65535

        class TerminateActivity(object):
            Operation_Completed_with_No_Error = pywbem.Uint32(0)
            Not_Supported = pywbem.Uint32(1)
            Unknown = pywbem.Uint32(2)
            Invalid_Activity_Identifer = pywbem.Uint32(3)
            # DMTF_Reserved = ..
            Method_Parameters_Checked___Job_Started = pywbem.Uint32(4096)
            # Method_Reserved = 4097..32767
            # Vendor_Specific = 32768..65535

        class AvailableRequestedStates(object):
            Enabled = pywbem.Uint16(2)
            Disabled = pywbem.Uint16(3)
            Shut_Down = pywbem.Uint16(4)
            Offline = pywbem.Uint16(6)
            Test = pywbem.Uint16(7)
            Defer = pywbem.Uint16(8)
            Quiesce = pywbem.Uint16(9)
            Reboot = pywbem.Uint16(10)
            Reset = pywbem.Uint16(11)
            # DMTF_Reserved = ..

        class Status(object):
            OK = 'OK'
            Error = 'Error'
            Degraded = 'Degraded'
            Unknown = 'Unknown'
            Pred_Fail = 'Pred Fail'
            Starting = 'Starting'
            Stopping = 'Stopping'
            Service = 'Service'
            Stressed = 'Stressed'
            NonRecover = 'NonRecover'
            No_Contact = 'No Contact'
            Lost_Comm = 'Lost Comm'
            Stopped = 'Stopped'

        class GetActivityStatus(object):
            Operation_Completed_with_No_Error = pywbem.Uint32(0)
            Not_Supported = pywbem.Uint32(1)
            Unknown = pywbem.Uint32(2)
            Invalid_Activity_Identifier = pywbem.Uint32(3)
            # DMTF_Reserved = ..
            Method_Parameters_Checked___Job_Started = pywbem.Uint32(4096)
            # Method_Reserved = 4097..32767
            # Vendor_Specific = 32768..65535

        class CommunicationStatus(object):
            Unknown = pywbem.Uint16(0)
            Not_Available = pywbem.Uint16(1)
            Communication_OK = pywbem.Uint16(2)
            Lost_Communication = pywbem.Uint16(3)
            No_Contact = pywbem.Uint16(4)
            # DMTF_Reserved = ..
            # Vendor_Reserved = 0x8000..

        class OperationalStatus(object):
            Unknown = pywbem.Uint16(0)
            Other = pywbem.Uint16(1)
            OK = pywbem.Uint16(2)
            Degraded = pywbem.Uint16(3)
            Stressed = pywbem.Uint16(4)
            Predictive_Failure = pywbem.Uint16(5)
            Error = pywbem.Uint16(6)
            Non_Recoverable_Error = pywbem.Uint16(7)
            Starting = pywbem.Uint16(8)
            Stopping = pywbem.Uint16(9)
            Stopped = pywbem.Uint16(10)
            In_Service = pywbem.Uint16(11)
            No_Contact = pywbem.Uint16(12)
            Lost_Communication = pywbem.Uint16(13)
            Aborted = pywbem.Uint16(14)
            Dormant = pywbem.Uint16(15)
            Supporting_Entity_in_Error = pywbem.Uint16(16)
            Completed = pywbem.Uint16(17)
            Power_Mode = pywbem.Uint16(18)
            Relocating = pywbem.Uint16(19)
            # DMTF_Reserved = ..
            # Vendor_Reserved = 0x8000..

        class OperatingStatus(object):
            Unknown = pywbem.Uint16(0)
            Not_Available = pywbem.Uint16(1)
            Servicing = pywbem.Uint16(2)
            Starting = pywbem.Uint16(3)
            Stopping = pywbem.Uint16(4)
            Stopped = pywbem.Uint16(5)
            Aborted = pywbem.Uint16(6)
            Dormant = pywbem.Uint16(7)
            Completed = pywbem.Uint16(8)
            Migrating = pywbem.Uint16(9)
            Emigrating = pywbem.Uint16(10)
            Immigrating = pywbem.Uint16(11)
            Snapshotting = pywbem.Uint16(12)
            Shutting_Down = pywbem.Uint16(13)
            In_Test = pywbem.Uint16(14)
            Transitioning = pywbem.Uint16(15)
            In_Service = pywbem.Uint16(16)
            # DMTF_Reserved = ..
            # Vendor_Reserved = 0x8000..

        class CreateActivity(object):
            Operation_Completed_with_No_Error = pywbem.Uint32(0)
            Not_Supported = pywbem.Uint32(1)
            Unknown = pywbem.Uint32(2)
            Not_Authorized = pywbem.Uint32(3)
            Not_Accepting_New_Activities = pywbem.Uint32(4)
            Unsupported_Feature = pywbem.Uint32(5)
            Invalid_Request_Message = pywbem.Uint32(6)
            # DMTF_Reserved = ..
            Method_Parameters_Checked___Job_Started = pywbem.Uint32(4096)
            # Method_Reserved = 4097..32767
            # Vendor_Specific = 32768..65535

        class GetAttributesDocument(object):
            Operation_Completed_with_No_Error = pywbem.Uint32(0)
            Not_Supported = pywbem.Uint32(1)
            Unknown = pywbem.Uint32(2)
            # DMTF_Reserved = ..
            Method_Parameters_Checked___Job_Started = pywbem.Uint32(4096)
            # Method_Reserved = 4097..32767
            # Vendor_Specific = 32768..65535

        class RequestStateChange(object):
            Completed_with_No_Error = pywbem.Uint32(0)
            Not_Supported = pywbem.Uint32(1)
            Unknown_or_Unspecified_Error = pywbem.Uint32(2)
            Cannot_complete_within_Timeout_Period = pywbem.Uint32(3)
            Failed = pywbem.Uint32(4)
            Invalid_Parameter = pywbem.Uint32(5)
            In_Use = pywbem.Uint32(6)
            # DMTF_Reserved = ..
            Method_Parameters_Checked___Job_Started = pywbem.Uint32(4096)
            Invalid_State_Transition = pywbem.Uint32(4097)
            Use_of_Timeout_Parameter_Not_Supported = pywbem.Uint32(4098)
            Busy = pywbem.Uint32(4099)
            # Method_Reserved = 4100..32767
            # Vendor_Specific = 32768..65535
            class RequestedState(object):
                Enabled = pywbem.Uint16(2)
                Disabled = pywbem.Uint16(3)
                Shut_Down = pywbem.Uint16(4)
                Offline = pywbem.Uint16(6)
                Test = pywbem.Uint16(7)
                Defer = pywbem.Uint16(8)
                Quiesce = pywbem.Uint16(9)
                Reboot = pywbem.Uint16(10)
                Reset = pywbem.Uint16(11)
                # DMTF_Reserved = ..
                # Vendor_Reserved = 32768..65535

        class StartMode(object):
            Automatic = 'Automatic'
            Manual = 'Manual'

        class PrimaryStatus(object):
            Unknown = pywbem.Uint16(0)
            OK = pywbem.Uint16(1)
            Degraded = pywbem.Uint16(2)
            Error = pywbem.Uint16(3)
            # DMTF_Reserved = ..
            # Vendor_Reserved = 0x8000..

        class GetActivityDocuments(object):
            Operation_Completed_with_No_Error = pywbem.Uint32(0)
            Not_Supported = pywbem.Uint32(1)
            Unknown = pywbem.Uint32(2)
            Invalid_Activity_Identifier = pywbem.Uint32(3)
            # DMTF_Reserved = ..
            Method_Parameters_Checked___Job_Started = pywbem.Uint32(4096)
            # Method_Reserved = 4097..32767
            # Vendor_Specific = 32768..65535

## end of class LMI_BasicExecutionServiceCondorFactoryProvider
    
## get_providers() for associating CIM Class Name to python provider class name
    
def get_providers(env): 
    lmi_basicexecutionservicecondorfactory_prov = LMI_BasicExecutionServiceCondorFactory(env)  
    return {'LMI_BasicExecutionServiceCondorFactory': lmi_basicexecutionservicecondorfactory_prov} 

# vim: ts=4:et:sw=4:tw=80:sts=4:cc=80
