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
import javax.cim.CIMArgument;
import javax.cim.CIMValuedElement;
import javax.cim.UnsignedInteger16;
import javax.wbem.WBEMException;
import javax.wbem.client.WBEMClient;
import javax.wbem.client.WBEMClientFactory;
import javax.wbem.client.UserPrincipal;
import javax.wbem.client.PasswordCredential;
import javax.wbem.CloseableIterator;
import javax.wbem.listener.IndicationListener;

class OpenLMIStorageClient {

    public static boolean retval;

    private final static String LV_STORAGE_EXTENT_CLASS_NAME = "LMI_LVStorageExtent";
    private static CIMObjectPath cop;
    private static WBEMClient cli;
    private static CIMInstance ins;

    public OpenLMIStorageClient(String hostname,
            String username,
            String password) {

        try {
            cli = WBEMClientFactory.getClient("CIM-XML");
            Subject subject = new Subject();
            subject.getPrincipals().add(new UserPrincipal(username));
            subject.getPrivateCredentials().add(new PasswordCredential(password));
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

    /**
     * This method helps to list all the available Logical Volumes in the system
     */
    public static List<CIMInstance> listLVs() {
        try {
           CIMObjectPath logicalVolumesPath =  new CIMObjectPath(null, null, null, "root/cimv2", LV_STORAGE_EXTENT_CLASS_NAME, null);
            final CloseableIterator<CIMInstance> iterator = cli.enumerateInstances(logicalVolumesPath, true, false, false, null);
            try {
                final List<CIMInstance> result = new ArrayList<CIMInstance>();
                while (iterator.hasNext()) {
                    final CIMInstance instance = iterator.next();
                    result.add(instance);
                }
            } finally {
                iterator.close();
            }

            return result;
        } catch (final WBEMException e) {
            e.printStackTrace();
        }
        return null;
    }
}