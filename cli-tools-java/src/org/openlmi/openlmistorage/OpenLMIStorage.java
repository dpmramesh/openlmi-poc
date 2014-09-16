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

package org.openlmi.openlmistorage;

import org.openlmi.openlmistorage.OpenLMIStorageClient;
import org.openlmi.openlmioptions.OpenLMIBasicOptions;
import java.lang.reflect.*;
import java.util.*;

class OpenLMIStorageOptions extends OpenLMIBasicOptions
{
       public OpenLMIStorageOptions() {
            super("Available actions:\n" +
            "lv-list disk-list\n");
    }
}

public class OpenLMIStorage
{
    private static int client_failed = 0;

    public static void main(String args[]) {
        System.out.println("OpenLMI Storage CIM Java client");

        OpenLMIStorageOptions options = new OpenLMIStorageOptions();
        options.parse(args);

        OpenLMIStorageClient client = new OpenLMIStorageClient(options.hostname,
                            options.username,
                            options.password);

        // Find instance for the service requested.
        List<CIMInstance> lvs= client.listLVs();
        for(CIMInstance instance: lvs){
            String name = instance.getProperty("Name").getValue().toString();
            System.out.println(name);
        }

       System.exit(client_failed);
    }
}
