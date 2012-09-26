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

package org.cura.curaoptions;

import org.kohsuke.args4j.CmdLineException;
import org.kohsuke.args4j.CmdLineParser;
import org.kohsuke.args4j.Option;
import org.kohsuke.args4j.Argument;
//import java.util.ArrayList;  
//import java.util.List;  

class MyOptions {
    
    @Option(name = "--help", aliases = "", 
            usage = "print this message")
    public boolean help = false;

    @Option(required=true, name="-h", aliases="--hostname", 
            usage="remote machine hostname", metaVar="HOSTNAME")
    public String hostname;

    @Option(name="-u", aliases="--username", 
            usage="remote machine username", metaVar="USERNAME")
    public String username;

    @Option(name="-p", aliases="--password", 
            usage="remote machine password", metaVar="PASSWORD")
    public String password;

    @Argument  
    public String poweraction;
}

public class CuraBasicOptions
{
    private CmdLineParser parser;
    private MyOptions opt;
    private String s;

    public String hostname;
    public String username;
    public String password;
    public String poweraction;

    public CuraBasicOptions() {
        opt = new MyOptions();
        parser = new CmdLineParser(opt);
    }

    public void parse(String args[]) {
        try {
            //for (String s: args) {
            //    System.out.println(s);
            //}
            parser.parseArgument(args);
            parser.setUsageWidth(80); // width of the error display area

        } catch(CmdLineException e) {
            System.err.println(e.getMessage());
            System.err.println("\nExample:\n java -cp " + 
                "/usr/share/java/sblim-cim-client2.jar:" + 
                "/usr/share/java/args4j.jar: " + 
                "CuraCli.jar org.cura.curapower.CuraPower [options]\n");
            parser.printUsage(System.err);
            return;
        }

        hostname = opt.hostname; 
        username = opt.username;
        password = opt.password;
        poweraction = opt.poweraction;
    }
}

/* vim: set ts=4 et sw=4 tw=0 sts=4 cc=80: */
