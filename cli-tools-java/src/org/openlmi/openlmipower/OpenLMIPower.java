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

package org.openlmi.openlmipower;

import org.openlmi.openlmipower.OpenLMIPowerClient;
import org.openlmi.openlmioptions.OpenLMIBasicOptions;
import java.lang.reflect.*;
import java.util.*;

class OpenLMIPowerOptions extends OpenLMIBasicOptions 
{
       public OpenLMIPowerOptions() {
            super("Available actions:\n" +
            "  poweroff, reboot, suspend, hibernate\n" +
            "  force-poweroff, force-reboot\n");
    }
}

class OpenLMIPower
{  
    private static int client_failed = 0;

    public static void main(String args[]) {
        System.out.println("OpenLMI Power CIM Java client");

        OpenLMIPowerOptions options = new OpenLMIPowerOptions();
        options.parse(args);

        OpenLMIPowerClient client = new OpenLMIPowerClient(options.hostname, 
                            options.username, 
                            options.password);
    
        HashMap<String, Method> powerActions = client.getPowerFn();

        if (!powerActions.containsKey(options.provideraction)) {
            System.err.println("No such action to perform!");
            System.exit(1);
        }

        try {
            powerActions.get(options.provideraction).invoke(null); 
        } catch (InvocationTargetException | IllegalAccessException e) {
            System.out.println(e);
        }
    
        if (client.retval) {
            System.out.println("success: " + options.hostname +
                               " " + options.provideraction);
        } else {
            System.err.println("error: " + options.hostname +
                               " " + options.provideraction);
            client_failed = 1;
        }

        System.exit(client_failed);
    }
}

/* vim: set ts=4 et sw=4 tw=0 sts=4 cc=80: */
