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

package org.cura.curapower;

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

class OpenLMIPowerClient {

    public static boolean retval;

    private final static String POWER_CLASS_NAME = "LMI_PowerManagementService";
    private final static int POWER_STATE_SUSPEND = 4;
    private final static int POWER_STATE_FORCE_REBOOT = 5;
    private final static int POWER_STATE_HIBERNATE = 7;
    private final static int POWER_STATE_FORCE_POWEROFF = 8;
    private final static int POWER_STATE_POWEROFF = 12;
    private final static int POWER_STATE_REBOOT = 15;
    private CIMObjectPath cop;
    private static WBEMClient cli;

    public OpenLMIPowerClient(String hostname,
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

    public static HashMap<String, Method> getPowerFn() {
        HashMap<String, Method> powerActions = new HashMap<String, Method>();

        try {
            powerActions.put("poweroff", 
                    OpenLMIPowerClient.class.getMethod("poweroff"));
            powerActions.put("reboot", 
                    OpenLMIPowerClient.class.getMethod("reboot"));
            powerActions.put("suspend", 
                    OpenLMIPowerClient.class.getMethod("suspend"));
            powerActions.put("hibernate", 
                    OpenLMIPowerClient.class.getMethod("hibernate"));
        } catch (NoSuchMethodException e) {
            System.out.println(e);
        }

       return powerActions;
    }

    private static CIMObjectPath __getPowerInstance() {
        CIMObjectPath instance = 
            new CIMObjectPath("/root/cimv2:" + POWER_CLASS_NAME);
        System.out.println(instance);
        return instance;
    }

    private static void __powerCallMethod(CIMObjectPath instance, 
                                            String method,
                                            int input_value) {
        CIMArgument<?>[] input = new CIMArgument[1];
        CIMArgument<?>[] output = new CIMArgument[0];

        CIMDataType d = new CIMDataType(CIMDataType.UINT16, 1);
        input[0] = new CIMArgument("PowerState", d,
                        new UnsignedInteger16(input_value));
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

    public static void poweroff() {
        __powerCallMethod(__getPowerInstance(),
                    "RequestPowerStateChange",
                    POWER_STATE_POWEROFF);
    }

    public static void reboot() {
        __powerCallMethod(__getPowerInstance(),
                    "RequestPowerStateChange",
                    POWER_STATE_REBOOT);
    }

    public static void suspend() {
        __powerCallMethod(__getPowerInstance(),
                    "RequestPowerStateChange",
                    POWER_STATE_SUSPEND);
    }

    public static void hibernate() {
        __powerCallMethod(__getPowerInstance(),
                    "RequestPowerStateChange",
                    POWER_STATE_HIBERNATE);
    }
}

/* vim: set ts=4 et sw=4 tw=0 sts=4 cc=80: */
