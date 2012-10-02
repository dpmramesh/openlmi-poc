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

import org.cura.curaservice.CuraServiceClient;
import org.cura.curaoptions.CuraBasicOptions;
import java.lang.reflect.*;
import java.util.*;

class CuraServiceOptions extends CuraBasicOptions 
{
       public CuraServiceOptions() {
            super("Available actions:\n" +
            "  start, stop, restart, enable, disable, reload,\n" +
            "  try-restart, cond-restart, reload-or-restart,\n" +
            "  reload-or-try-restart, status\n");
    }
}

class CuraService
{  
    private static int client_failed = 0;

    public static void main(String args[]) {
        System.out.println("Cura Service CIM Java client");

        CuraServiceOptions options = new CuraServiceOptions();
        options.parse(args);

        CuraServiceClient client = new CuraServiceClient(options.hostname, 
                            options.username, 
                            options.password);
    
        client.serviceFind(options.servicename);

        HashMap<String, Method> serviceActions = client.getServiceFn();

        if (!serviceActions.containsKey(options.provideraction)) {
            System.err.println("No such action to perform!");
            System.exit(1);
        }

        try {
            serviceActions.get(options.provideraction).invoke(null); 
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
