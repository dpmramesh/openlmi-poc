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
import javax.cim.CIMObjectPath;
import javax.wbem.WBEMException;
import javax.wbem.client.WBEMClient;
import javax.wbem.client.WBEMClientFactory;
import javax.wbem.client.UserPrincipal;
import javax.cim.CIMArgument;
import javax.wbem.CloseableIterator;
import javax.cim.CIMInstance;
import javax.cim.CIMValuedElement;
import javax.cim.UnsignedInteger16;
import javax.wbem.listener.IndicationListener;

class CuraServiceClient {

    public static boolean retval;

    private final static String SERVICE_CLASS_NAME = "LMI_Service";
    private CIMObjectPath cop;
    private static WBEMClient cli;

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

    public static HashMap<String, Method> getServiceFn() {
        HashMap<String, Method> serviceActions = new HashMap<String, Method>();

        try {
            serviceActions.put("start", 
                    CuraServiceClient.class.getMethod("start"));
            serviceActions.put("stop", 
                    CuraServiceClient.class.getMethod("stop"));
            serviceActions.put("restart", 
                    CuraServiceClient.class.getMethod("restart"));
            serviceActions.put("enable", 
                    CuraServiceClient.class.getMethod("enable"));
            serviceActions.put("disable", 
                    CuraServiceClient.class.getMethod("disable"));
            serviceActions.put("reload", 
                    CuraServiceClient.class.getMethod("reload"));
            serviceActions.put("try-restart", 
                    CuraServiceClient.class.getMethod("tryrestart"));
            serviceActions.put("cond-restart", 
                    CuraServiceClient.class.getMethod("condrestart"));
            serviceActions.put("reload-or-restart", 
                    CuraServiceClient.class.getMethod("reloadorrestart"));
            serviceActions.put("reload-or-try-restart", 
                    CuraServiceClient.class.getMethod("reloadortryrestart"));
            serviceActions.put("status",
                    CuraServiceClient.class.getMethod("status"));
        } catch (NoSuchMethodException e) {
            System.out.println(e);
        }

       return serviceActions;
    }

    private static CIMObjectPath __getServiceInstance() {
        CIMObjectPath instance = 
            new CIMObjectPath("/root/cimv2:" + SERVICE_CLASS_NAME);
        System.out.println(instance);
        return instance;
    }

    private static void __serviceCallMethod(CIMObjectPath instance, 
                                            String method) {
        CIMArgument<?>[] input = new CIMArgument[1];
        CIMArgument<?>[] output = new CIMArgument[0];

        CIMDataType d = new CIMDataType(CIMDataType.UINT16, 1);
        //input[0] = new CIMArgument("ServiceState", d,
         //               new UnsignedInteger16(input_value));
        try {
            Object obj = 
                cli.invokeMethod(instance, method, input, output);

                System.out.println("result: " + obj);
                retval = true;
        } catch(WBEMException e){
                System.out.println(e);
                retval = false;
        }
    }

    public static void start() {
        __serviceCallMethod(__getServiceInstance(), "StartService");
    }

    public static void stop() {
        __serviceCallMethod(__getServiceInstance(), "StopService");
    }

    public static void restart() {
        __serviceCallMethod(__getServiceInstance(), "RestartService");
    }

    public static void enable() {
        __serviceCallMethod(__getServiceInstance(), "TurnServiceOn");
    }

    public static void disable() {
        __serviceCallMethod(__getServiceInstance(), "iTurnServiceOff");
    }

    public static void reload() {
        __serviceCallMethod(__getServiceInstance(), "ReloadService");
    }

    public static void tryrestart() {
        __serviceCallMethod(__getServiceInstance(), "TryRestartService");
    }

    public static void condrestart() {
        __serviceCallMethod(__getServiceInstance(), "CondRestartService");
    }

    public static void reloadorrestart() {
        __serviceCallMethod(__getServiceInstance(), "ReloadOrRestartService");
    }

    public static void reloadortryrestart() {
        __serviceCallMethod(__getServiceInstance(), "ReloadOrTryRestartService");
    }

    public static void status() {
        __serviceCallMethod(__getServiceInstance(), "Status");
    }
}

/* vim: set ts=4 et sw=4 tw=0 sts=4 cc=80: */
