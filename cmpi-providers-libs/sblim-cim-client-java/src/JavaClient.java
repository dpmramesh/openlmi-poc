//import java.util.Vector;
//import java.io.IOException;
import javax.security.auth.Subject;
import java.util.Iterator;

import javax.cim.CIMDataType;
import javax.cim.CIMClass;
import javax.cim.CIMInstance;
import javax.cim.CIMObjectPath;
import javax.wbem.WBEMException;
import javax.wbem.client.WBEMClient;
import javax.wbem.client.WBEMClientFactory;
import javax.wbem.client.UserPrincipal;
import javax.cim.CIMArgument;
import javax.wbem.CloseableIterator;
import javax.cim.CIMInstance;

class JavaClient
{  
public static void main(String args[])
		{
				System.out.println("CIM Java client");

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

						CIMArgument<?>[] input = new CIMArgument[2];
						CIMArgument<?>[] output = new CIMArgument[2];
/*
						input[0] = new CIMArgument("X", new CIMDataType(UINT32), 1);
						input[1] = new CIMArgument("Y", CIMDataType.UINT32, 1);

						Object obj = 
								cli.invokeMethod(new CIMObjectPath("/root/cimv2:KC_Widget"), 
												"Add", input, output);

						if (obj.toString().equals("0")) 
						{
								System.out.println("Indication generated successfully...");
						}

*/
				} catch (WBEMException e) {
						// Print out the exception that occurred
						System.out.println(e);

				}
		}
}

