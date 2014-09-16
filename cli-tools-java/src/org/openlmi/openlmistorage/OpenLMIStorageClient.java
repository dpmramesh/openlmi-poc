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

import java.util.ArrayList;
import java.util.List;

import javax.cim.CIMArgument;
import javax.cim.CIMDataType;
import javax.cim.CIMInstance;
import javax.cim.CIMObjectPath;
import javax.cim.UnsignedInteger64;
import javax.security.auth.Subject;
import javax.wbem.CloseableIterator;
import javax.wbem.WBEMException;
import javax.wbem.client.PasswordCredential;
import javax.wbem.client.UserPrincipal;
import javax.wbem.client.WBEMClient;
import javax.wbem.client.WBEMClientFactory;

class OpenLMIStorageClient {

    public static boolean retval;

    private final static String LV_STORAGE_EXTENT_CLASS_NAME = "LMI_LVStorageExtent";
    private final static String LMI_STORAGE_EXTENT_CLASS_NAME = "LMI_StorageExtent";
    private final static String LMI_STORAGE_CONFIGURATION_SERVICE_CLASS_NAME = "LMI_StorageConfigurationService";
    private final static String LMI_VG_STORAGE_POOL_CLASS_NAME = "LMI_VGStoragePool";
    private static CIMObjectPath cop;
    private static WBEMClient cli;

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
    public List<LogicalVolume> listLVs() {
        try {
            CIMObjectPath logicalVolumesPath =
                    new CIMObjectPath(null, null, null, "root/cimv2", LV_STORAGE_EXTENT_CLASS_NAME, null);
            final CloseableIterator<CIMInstance> iterator =
                    cli.enumerateInstances(logicalVolumesPath, true, false, false, null);
            final List<LogicalVolume> result = new ArrayList<LogicalVolume>();
            try {
                while (iterator.hasNext()) {
                    final CIMInstance instance = iterator.next();
                    String lvName = instance.getProperty("Name").getValue().toString();
                    String blockSize = instance.getProperty("BlockSize").getValue().toString();
                    String noOfBlocks = instance.getProperty("NumberOfBlocks").getValue().toString();
                    result.add(new LogicalVolume(lvName, blockSize, noOfBlocks));
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

    /**
     * This method helps to list all the available Logical Volumes in the system
     */
    public List<LogicalVolume> listDisks() {
        try {
            CIMObjectPath logicalVolumesPath =
                    new CIMObjectPath(null, null, null, "root/cimv2", LMI_STORAGE_EXTENT_CLASS_NAME, null);
            final CloseableIterator<CIMInstance> iterator =
                    cli.enumerateInstances(logicalVolumesPath, true, false, false, null);
            final List<LogicalVolume> result = new ArrayList<LogicalVolume>();
            try {
                while (iterator.hasNext()) {
                    final CIMInstance instance = iterator.next();
                    if ("True".equalsIgnoreCase(instance.getProperty("Primordial").getValue().toString())) {
                        String lvName = instance.getProperty("Name").getValue().toString();
                        String blockSize = instance.getProperty("BlockSize").getValue().toString();
                        String noOfBlocks = instance.getProperty("NumberOfBlocks").getValue().toString();
                        result.add(new LogicalVolume(lvName, blockSize, noOfBlocks));
                    }
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

    public CIMInstance getStorageExtentInstance(String name) {
        String query = "select * from " + LMI_STORAGE_EXTENT_CLASS_NAME + " where DeviceID=\"" + name + "\"";
        CIMObjectPath cimv2Path =
                new CIMObjectPath(null, null, null, "root/cimv2", LMI_STORAGE_EXTENT_CLASS_NAME, null);

        try {
            final CloseableIterator<CIMInstance> iterator = cli.execQuery(cimv2Path, query, "WQL");
            while (iterator.hasNext()) {
                final CIMInstance instance = iterator.next();
                if (instance.getProperty("DeviceID").getValue().toString().equalsIgnoreCase(name)) {
                    iterator.close();
                    return instance;
                }
            }
            return null;
        } catch (final WBEMException e) {
            e.printStackTrace();
        }
        return null;
    }

    public CIMInstance getStorageConfigurationService(){
        String query = "select * from " + LMI_STORAGE_CONFIGURATION_SERVICE_CLASS_NAME;
        CIMObjectPath cimv2Path =
                new CIMObjectPath(null, null, null, "root/cimv2", LMI_STORAGE_CONFIGURATION_SERVICE_CLASS_NAME, null);

        try {
            final CloseableIterator<CIMInstance> iterator = cli.execQuery(cimv2Path, query, "WQL");
            while (iterator.hasNext()) {
                final CIMInstance instance = iterator.next();
                return instance;
            }
            return null;
        } catch (final WBEMException e) {
            e.printStackTrace();
        }
        return null;
    }

    public CIMInstance getStoragePool(String name) {
        String query =
                "select * from " + LMI_VG_STORAGE_POOL_CLASS_NAME + " where ElementName=\"" + name + "\"";
        CIMObjectPath cimv2Path =
                new CIMObjectPath(null, null, null, "root/cimv2", LMI_VG_STORAGE_POOL_CLASS_NAME, null);

        try {
            final CloseableIterator<CIMInstance> iterator = cli.execQuery(cimv2Path, query, "WQL");
            while (iterator.hasNext()) {
                final CIMInstance instance = iterator.next();
                return instance;
            }
            return null;
        } catch (final WBEMException e) {
            e.printStackTrace();
        }
        return null;
    }

    public void createVolumeGroup(String vgName, List<String> diskIdList) {
        CIMArgument<?>[] input = new CIMArgument[2];
        CIMArgument<?>[] output = new CIMArgument[3];
        CIMDataType stringType = new CIMDataType(CIMDataType.STRING, 1);
        input[0] = new CIMArgument("ElementName", stringType, vgName);
        List<CIMInstance> diskInstances = new ArrayList<CIMInstance>();

        for(String disk:diskIdList){
            CIMInstance instance = getStorageExtentInstance(disk);
            if(instance != null){
                diskInstances.add(instance);
                System.out.println("Disk " + instance.getProperty("Name").getValue().toString());
            }else{
                System.out.println("Disk " + disk + " doesn't exists");
            }
        }
        input[1] = new CIMArgument("InExtents", CIMDataType.OBJECT_ARRAY_T, diskInstances.toArray(new CIMInstance[diskInstances.size()]));
        try {
            CIMInstance storageConfigService = getStorageConfigurationService();
            cli.invokeMethod(storageConfigService.getObjectPath(), "CreateOrModifyVG", input, output);
            System.out.println(output);
        } catch (WBEMException e) {
            e.printStackTrace();
        }
    }

    public void createLV(String vgName, String lvName, String sizeInBytes) {
        CIMArgument<?>[] input = new CIMArgument[3];
        CIMArgument<?>[] output = new CIMArgument[2];
        CIMDataType stringType = new CIMDataType(CIMDataType.STRING, 1);
        CIMDataType uInt64Type = new CIMDataType(CIMDataType.UINT64, 1);
        input[0] = new CIMArgument("ElementName", stringType, lvName);
        input[1] = new CIMArgument("InPool", CIMDataType.OBJECT_T, getStoragePool(vgName));
        input[2] = new CIMArgument("Size", uInt64Type, new UnsignedInteger64(sizeInBytes));

        try {
            CIMInstance storageConfigService = getStorageConfigurationService();
            cli.invokeMethod(storageConfigService.getObjectPath(), "CreateOrModifyLV", input, output);
            System.out.println(output);
        } catch (WBEMException e) {
            e.printStackTrace();
        }
    }
}
