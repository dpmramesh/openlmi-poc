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

import org.cura.curapower.CuraPowerClient;
import org.cura.curaoptions.CuraBasicOptions;
import java.util.List;
import java.util.ArrayList;

class CuraPower
{  
    public static void main(String args[]) {
        System.out.println("Cura Power CIM Java client");

        List<String> powerActions = new ArrayList<String>();

        powerActions.add("poweroff");
        powerActions.add("reboot");
        powerActions.add("suspend");
        powerActions.add("hibernate");

        CuraBasicOptions options = new CuraBasicOptions();
        options.parse(args);

        CuraPowerClient client = new CuraPowerClient(options.hostname, 
                            options.username, 
                            options.password);

        if (!powerActions.contains(options.poweraction)) {
            System.err.println("No such action to perform!");
        } 
    }
}

/* vim: set ts=4 et sw=4 tw=0 sts=4 cc=80: */
