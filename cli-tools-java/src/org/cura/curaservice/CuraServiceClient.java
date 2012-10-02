// Copyright (C) 2012  Javi Roman <javiroman@kernel-labs.org>
//
// This program is free software; you can redistribute it and/or
// modify it under the terms of the GNU General Public License
// as published by the Free Software Foundation; either version 2
// of the License, or (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program; if not, see <http://www.gnu.org/licenses/>.

package org.cura.curaservice;

import java.io.IOException; 
import javax.security.auth.Subject;
import java.util.Iterator;
import java.lang.InterruptedException;
import java.lang.reflect.*;
import java.util.*;

import javax.cim.CIMClass;
import javax.cim.CIMDataType;
import javax.cim.CIMInstance;
import javax.cim.CIMProperty;
import javax.cim.CIMObjectPath;
import javax.wbem.WBEMException;
import javax.wbem.client.WBEMClient;
import javax.wbem.client.WBEMClientFactory;
import javax.wbem.client.UserPrincipal;
import javax.cim.CIMArgument;
import javax.wbem.CloseableIterator;
import javax.cim.CIMValuedElement;
import javax.cim.UnsignedInteger16;
import javax.wbem.listener.IndicationListener;

class CuraServiceClient {

    public static boolean retval;

    private final static String SERVICE_CLASS_NAME = "LMI_Service";
    private static CIMObjectPath cop;
    private static WBEMClient cli;
    private static CIMInstance ins;

    public CuraServiceClient(String hostname,
                                  String username,
                                  String password) {

        try {
            cli = WBEMClientFactory.getClient("CIM-XML");
            Subject subject = new Subject();

            cop = new CIMObjectPath("https", 
                                hostname, 
                                "5989", 
                                "/root/cimv2",
                                null,
                                null);
            cli.initialize(cop, subject, null);

        } catch (WBEMException e) {
            System.out.println(e);
        }
    }

    public void serviceFind(String service_name) {
        ins = __serviceGetInstance(service_name);
    }

    public static HashMap<String, Method> getServiceFn() {
        HashMap<String, Method> serviceActions = new HashMap<String, Method>();

        try {
            serviceActions.put("start", 
                    CuraServiceClient.class.getMethod("serviceStart"));
            serviceActions.put("stop", 
                    CuraServiceClient.class.getMethod("serviceStop"));
            serviceActions.put("restart", 
                    CuraServiceClient.class.getMethod("serviceRestart"));
            serviceActions.put("enable", 
                    CuraServiceClient.class.getMethod("serviceEnable"));
            serviceActions.put("disable", 
                    CuraServiceClient.class.getMethod("serviceDisable"));
            serviceActions.put("reload", 
                    CuraServiceClient.class.getMethod("serviceReload"));
            serviceActions.put("try-restart", 
                    CuraServiceClient.class.getMethod("serviceTryRestart"));
            serviceActions.put("cond-restart", 
                    CuraServiceClient.class.getMethod("serviceCondRestart"));
            serviceActions.put("reload-or-restart", 
                    CuraServiceClient.class.getMethod("serviceReloadRestart"));
            serviceActions.put("reload-or-try-restart", 
                    CuraServiceClient.class.getMethod("serviceReloadTryRestart"));
            serviceActions.put("status",
                    CuraServiceClient.class.getMethod("serviceStatus"));
        } catch (NoSuchMethodException e) {
            System.err.println("error en hashmap");
            System.out.println(e);
        }

       return serviceActions;
    }

    private static CIMInstance __serviceGetInstance(String s) {
        //String name = "";
        boolean find = false;
        CIMInstance instance;
		try {
    	    final CloseableIterator<CIMInstance> iterator = 
                cli.enumerateInstances(
			        new CIMObjectPath(null, null, null, 
                                "root/cimv2", SERVICE_CLASS_NAME, null), 
                        true, false, false, null);
        	try {
				final List<CIMInstance> result = new ArrayList<CIMInstance>();
				while (iterator.hasNext()) {
					final CIMInstance tmpinstance = iterator.next();
                    String name = new 
                        String(tmpinstance.getProperty("Name").getValue().toString());
                    if (s.equals(name)) {
                        System.out.println(tmpinstance);
                        find = true;
                        break;
                    }
				}
                if (find) {
                    System.out.println("service " + s + " match!");

			        CIMProperty<String> nameservice = 
                        new CIMProperty<String>("Name", CIMDataType.STRING_T,
					"httpd", true, false, null);
                    CIMProperty<?>[] properties = new CIMProperty[] { nameservice};
                    
		            final CIMObjectPath path = 
			                new CIMObjectPath(null, null, null, 
                                "root/cimv2", SERVICE_CLASS_NAME, null, null);
                    instance = new CIMInstance(path, properties);
                } else {
                    System.out.println("No such service " + s + " found!"); 
				    return null;
                }
			} finally {
				iterator.close();
            }

            return instance;
		} catch (final WBEMException e) {
			e.printStackTrace();
		}

    /*
        CIMObjectPath instance = 
            new CIMObjectPath("/root/cimv2:" + SERVICE_CLASS_NAME, s);
        System.out.println(instance);
        return instance;
    */
		return null;
    }

    private static int __serviceGetProperty(CIMInstance instance,
                                            String method) {
        System.out.println("status -> ...");
        return 0;
    }

    private static void __serviceCallMethod(CIMInstance instance, 
                                            String method) {

        CIMArgument<?>[] input = new CIMArgument[0];
        CIMArgument<?>[] output = new CIMArgument[0];

        try {
            Object obj = 
                cli.invokeMethod(instance.getObjectPath(), 
                                 method, input, output);

                System.out.println("result: " + obj);
                retval = true;
        } catch(WBEMException e){
                System.out.println(e);
                retval = false;
        }
    }

    public static void serviceStart() {
        __serviceCallMethod(ins, "StartService");
    }

    public static void serviceStop() {
        __serviceCallMethod(ins, "StopService");
    }

    public static void serviceRestart() {
        __serviceCallMethod(ins, "RestartService");
    }

    public static void serviceEnable() {
        __serviceCallMethod(ins, "TurnServiceOn");
    }

    public static void serviceDisable() {
        __serviceCallMethod(ins, "TurnServiceOff");
    }

    public static void serviceReload() {
        __serviceCallMethod(ins, "ReloadService");
    }

    public static void serviceTryRestart() {
        __serviceCallMethod(ins, "TryRestartService");
    }

    public static void serviceCondRestart() {
        __serviceCallMethod(ins, "CondRestartService");
    }

    public static void serviceReloadRestart() {
        __serviceCallMethod(ins, "ReloadOrRestartService");
    }

    public static void serviceReloadTryRestart() {
        __serviceCallMethod(ins, "ReloadOrTryRestartService");
    }

    public static void serviceStatus() {
       __serviceGetProperty(ins, "Status");
    }
}

/* vim: set ts=4 et sw=4 tw=0 sts=4 cc=80: */
