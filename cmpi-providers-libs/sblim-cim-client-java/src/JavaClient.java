import javax.security.auth.Subject;
import java.util.Iterator;
import java.lang.InterruptedException;

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
import javax.cim.UnsignedInteger32;
import javax.wbem.listener.IndicationListener;

class JavaClient
{  
	public static void invokeCIMMethod() {
        try {
			WBEMClient cli = WBEMClientFactory.getClient("CIM-XML");
		    Subject subject = new Subject();
		    //subject.getPrincipals().add(new UserPrincipal(""));
            //subject.getPrivateCredentials().add(new PasswordCredential(""));
            //PasswordCredential password = new PasswordCredential("userPassword");
            CIMObjectPath cop = new CIMObjectPath("https", 
                                    "localhost", 
                                    "5989", 
                                    "/root/cimv2",
                                    null,
                                    null);

            System.out.println(cop.getHost()); 
            System.out.println(cop.getNamespace()); 
            System.out.println(cop.getPort()); 

            cli.initialize(cop, subject, null);

            CloseableIterator itr = cli.execQuery(cop, "select * from KC_Widget", "WQL");

            while(itr.hasNext()) {
                Object element = itr.next(); 
                System.out.print(element + "\n");
            } 

            // Two inputs arguments to pass to method Add()
            CIMArgument<?>[] input = new CIMArgument[2];
            // Two output value returns, the addition result and the error code
            CIMArgument<?>[] output = new CIMArgument[1];

            CIMDataType d = new CIMDataType(CIMDataType.UINT32, 1);
            CIMDataType dd = new CIMDataType(CIMDataType.UINT32, 1);

            input[0] = new CIMArgument("X", d, new UnsignedInteger32(7));
            input[1] = new CIMArgument("Y", dd, new UnsignedInteger32(7));
	
            Object obj = 
                cli.invokeMethod(new CIMObjectPath("/root/cimv2:KC_Widget"), 
                                 "Add", input, output);
        
            try {
                Thread.sleep(1000);

                if (obj.toString().equals("0")) {
                    System.out.println("Method not invoked successfully!");
                } else {
                    System.out.println("Method invoked successfully!");
                    System.out.println("result: " + obj);
                }

            } catch(InterruptedException ie){
                System.out.println(ie);
            }

        } catch (WBEMException e) {
            System.out.println(e);
        }
    }

    public static void main(String args[]) {
        System.out.println("CIM Java client");
        invokeCIMMethod();
    }
}

/* vim: set ts=4 et sw=4 tw=0 sts=4: */