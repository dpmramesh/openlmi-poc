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

import java.util.Arrays;
import java.util.List;

import org.openlmi.openlmioptions.OpenLMIBasicOptions;

class OpenLMIStorageOptions extends OpenLMIBasicOptions
{
    public OpenLMIStorageOptions() {
        super("Available actions:\n" +
                "lv-list disk-list vg-create lv-create\n");
    }
}

public class OpenLMIStorage
{
    public static void main(String args[]) {
        System.out.println("OpenLMI Storage CIM Java client");

        OpenLMIStorageOptions options = new OpenLMIStorageOptions();
        options.parse(args);

        OpenLMIStorageClient client = new OpenLMIStorageClient(options.hostname,
                options.username,
                options.password);
        String vgName = "";
        String lvName = "";
        String size;
        switch (options.provideraction) {
        case "lv-list":
            // Find instance for the service requested.
            List<LogicalVolume> lvs = client.listLVs();
            System.out.println("Logical Volumes in the host : " + options.hostname);
            for (LogicalVolume lv : lvs) {
                System.out.println(lv.getName() + " " + lv.getBlockSize() + "*" + lv.getNoOfBlocks());
            }
            break;
        case "disk-list":
            // Find instance for the service requested.
            List<LogicalVolume> disks = client.listDisks();
            System.out.println("Disks in the host : " + options.hostname);
            for (LogicalVolume disk : disks) {
                System.out.println(disk.getName() + " " + disk.getBlockSize() + "*" + disk.getNoOfBlocks());
            }
            break;
        case "vg-create":
            vgName = "vg1";
            List<String> diskIdList = Arrays.asList("/dev/vde", "/dev/vdf");
            client.createVolumeGroup(vgName, diskIdList);
            break;

        case "lv-create":
            vgName = "vg1";
            lvName = "lv1";
            size = "333333333";
            client.createLV(vgName, lvName, size);
            break;
        default:
            System.out.println("Option : " + options.provideraction + " is not supported");
            break;
        }
        System.exit(0);
    }
}
