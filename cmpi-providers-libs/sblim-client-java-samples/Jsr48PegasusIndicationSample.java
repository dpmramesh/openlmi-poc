/**
 * (C) Copyright IBM Corp. 2011, 2012
 *
 * THIS FILE IS PROVIDED UNDER THE TERMS OF THE ECLIPSE PUBLIC LICENSE
 * ("AGREEMENT"). ANY USE, REPRODUCTION OR DISTRIBUTION OF THIS FILE
 * CONSTITUTES RECIPIENTS ACCEPTANCE OF THE AGREEMENT.
 *
 * You can obtain a current copy of the Eclipse Public License from
 * http://www.opensource.org/licenses/eclipse-1.0.php
 *
 * @author : Alexander Wolf-Reber, a.wolf-reber@de.ibm.com
 * @author : Dave Blaschke, blaschke@us.ibm.com
 *
 * Flag       Date        Prog         Description
 * -------------------------------------------------------------------------------
 * 3182121    2011-02-15  blaschke-oss Add Jsr48PegasusIndicationSample
 * 3185818    2011-02-18  blaschke-oss indicationOccured URL incorrect
 * 3267429    2011-04-01  blaschke-oss Samples should close client
 * 3374206    2011-07-22  blaschke-oss NullPointerException caused by Indication
 * 3469018    2012-01-03  blaschke-oss Properties not passed to CIMIndicationHandler
 * 3480115    2012-01-26  blaschke-oss Add Jsr48SfcbIndicationSample
 * 3477087    2012-01-23  blaschke-oss Need Access to an Indication Sender's IP Address
 * 3521119    2012-04-24  blaschke-oss JSR48 1.0.0: remove CIMObjectPath 2/3/4-parm ctors
 */
package org.sblim.cimclient.samples;

import java.io.IOException;
import java.net.InetAddress;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.UnknownHostException;
import java.util.Properties;

import javax.cim.CIMArgument;
import javax.cim.CIMDataType;
import javax.cim.CIMInstance;
import javax.cim.CIMObjectPath;
import javax.cim.CIMProperty;
import javax.wbem.WBEMException;
import javax.wbem.client.WBEMClient;
import javax.wbem.client.WBEMClientConstants;
import javax.wbem.listener.IndicationListener;
import javax.wbem.listener.WBEMListener;
import javax.wbem.listener.WBEMListenerFactory;

import org.sblim.cimclient.IndicationListenerSBLIM;
import org.sblim.cimclient.WBEMListenerSBLIM;

/**
 * Class Jsr48PegasusIndicationSample is an example for setting up an indication
 * listener with the JSR48 API and receiving a test indication from an
 * OpenPegasus provider that is included in its SDK.
 * 
 * The following steps need to be performed on the CIMOM (OpenPegasus) prior to
 * running this sample:
 * 
 * 1) Start CIMOM (if not already started)
 * 
 * <pre>
 * /etc/init.d/tog-pegasus start
 * </pre>
 * 
 * 2) Compile base schema to SDKExamples namespace
 * 
 * <pre>
 * cimmof -n SDKExamples/DefaultCXX $PEGASUS_ROOT/Schemas/CIM217/DMTF/qualifiers.mof
 * cimmof -n SDKExamples/DefaultCXX $PEGASUS_ROOT/Schemas/CIM217/DMTF/Core/CIM_ManagedElement.mof
 * cimmof -n SDKExamples/DefaultCXX $PEGASUS_ROOT/Schemas/CIM217/CIM_Core.mof
 * cimmof -n SDKExamples/DefaultCXX $PEGASUS_ROOT/Schemas/CIM217/CIM_Event.mof
 * </pre>
 * 
 * 3) Compile provider MOF to SDKExamples namespace
 * 
 * <pre>
 * cimmof -n SDKExamples/DefaultCXX $PEGASUS_ROOT/src/SDK/samples/Providers/Load/SampleProviderSchema.mof
 * </pre>
 * 
 * 4) Register provider with CIMOM
 * 
 * <pre>
 * cimmof -n root/PG_InterOp $PEGASUS_ROOT/src/SDK/samples/Providers/Load/IndicationProviderR.mof
 * </pre>
 * 
 * 5) Build shared library
 * 
 * <pre>
 * cd $PEGASUS_ROOT/src/SDK/samples/Providers/DefaultC++/IndicationProvider
 * make
 * </pre>
 * 
 * 6) Stop CIMOM
 * 
 * <pre>
 * /etc/init.d/tog-pegasus stop
 * </pre>
 * 
 * 7) Start CIMOM
 * 
 * <pre>
 * /etc/init.d/tog-pegasus start
 * </pre>
 * 
 * At this point, an instance of RT_TestIndication can be generated by invoking
 * the method SendTestIndication of RT_TestIndication on the CIMOM. That is
 * accomplished by running this sample.
 * 
 * This example is based on the article "Generate dummy CIM indications for
 * testing on Linux" on developerWorks:
 * 
 * http://www.ibm.com/developerworks/opensource/library/l-cim-test/index.html
 */
public class Jsr48PegasusIndicationSample {

	private static final String PROTOCOL = "http";

	private static final String LISTENER_PORT = "5999";

	// Namespace where indication provider is registered
	private static final String PROVIDER_NAMESPACE = "root/PG_Interop";

	// Namespace where indication originates
	private static final String INDICATION_NAMESPACE = "SDKExamples/DefaultCXX";

	private static CIMObjectPath cSubscriptionPath;

	private static CIMObjectPath cFilterPath;

	private static CIMObjectPath cDestinationPath;

	private static WBEMListener cListener;

	private static int cId = 0;

	/**
	 * Starts a listener. The JSR48 library will open a HTTP(S) server socket
	 * and listen for incoming indications on that socket. Any indications
	 * received will be forwarded to the registered IndicationListener
	 * implementation. The sample one here just prints the indication to stdout
	 * along with a message indicating whether the CIMOM supports reliable
	 * indications.
	 * 
	 * @return <code>true</code> if the listener could be started,
	 *         <code>false</code> otherwise.
	 */
	public static boolean startListener() {
		try {
			cListener = WBEMListenerFactory.getListener(WBEMClientConstants.PROTOCOL_CIMXML);
			cListener.addListener(new IndicationListener() {

				public void indicationOccured(String pIndicationURL, CIMInstance pIndication) {
					System.out.println("Indication received on: " + pIndicationURL + ":");
					try {
						URL parsedURL = new URL(pIndicationURL);
						System.out.println("The URL could be parsed, path is: "
								+ parsedURL.getPath());
					} catch (MalformedURLException e) {
						System.out.println("The URL could NOT be parsed: " + e);
					}
					System.out.println(Jsr48CimSample.toMof(pIndication));
					CIMProperty<?> context = pIndication.getProperty("SequenceContext");
					CIMProperty<?> number = pIndication.getProperty("SequenceNumber");
					System.out.println("Based on content of indication, CIMOM DOES"
							+ (context == null || number == null || context.getValue() == null
									|| number.getValue() == null ? " NOT " : " ")
							+ "support reliable indications.");
				}
			}, Integer.parseInt(LISTENER_PORT), PROTOCOL);

			return true;

		} catch (IOException e) {
			// nothing to do here
		}
		return false;
	}

	/**
	 * Starts a reliable listener. The JSR48 library will open a HTTP(S) server
	 * socket and listen for incoming indications on that socket. Any
	 * indications received will be forwarded to the registered
	 * IndicationListener implementation. The sample one here just prints the
	 * indication to stdout along with a message indicating whether the CIMOM
	 * supports reliable indications.
	 * 
	 * @return <code>true</code> if the listener could be started,
	 *         <code>false</code> otherwise.
	 */
	public static boolean startReliableListener() {
		try {
			cListener = WBEMListenerFactory.getListener(WBEMClientConstants.PROTOCOL_CIMXML);

			// Cast WBEMListener to WBEMListenerSBLIM to get access to the
			// addListener() method that accepts properties - this method is not
			// part of the JSR48 standard, but is a SBLIM addition
			WBEMListenerSBLIM sListener = (WBEMListenerSBLIM) cListener;

			// Enable reliable indications using 2 retries at intervals of 30
			// seconds
			Properties props = new Properties();
			props.setProperty("sblim.wbem.listenerEnableReliableIndications", "true");
			props.setProperty("sblim.wbem.listenerDeliveryRetryAttempts", "2");
			props.setProperty("sblim.wbem.listenerDeliveryRetryInterval", "30");

			sListener.addListener(new IndicationListenerSBLIM() {

				public void indicationOccured(String pIndicationURL, CIMInstance pIndication,
						InetAddress pSenderAddress) {
					System.out.println("Indication received on: " + pIndicationURL + ": from IP: "
							+ pSenderAddress.getHostAddress());
					try {
						URL parsedURL = new URL(pIndicationURL);
						System.out.println("The URL could be parsed, path is: "
								+ parsedURL.getPath());
					} catch (MalformedURLException e) {
						System.out.println("The URL could NOT be parsed: " + e);
					}
					System.out.println(Jsr48CimSample.toMof(pIndication));
					CIMProperty<?> context = pIndication.getProperty("SequenceContext");
					CIMProperty<?> number = pIndication.getProperty("SequenceNumber");
					System.out.println("Based on content of indication, CIMOM DOES"
							+ (context == null || number == null || context.getValue() == null
									|| number.getValue() == null ? " NOT " : " ")
							+ "support reliable indications.");
				}
			}, Integer.parseInt(LISTENER_PORT), PROTOCOL, null, props);

			return true;

		} catch (IOException e) {
			// nothing to do here
		}
		return false;
	}

	/**
	 * Constructs a CIM_ListenerDestinationCIMXML instance
	 * 
	 * @param pNamespace
	 *            The scoping namespace
	 * @param pURL
	 *            The URL of the destination
	 * @return The instance
	 */
	private static CIMInstance makeListenerDestination(String pNamespace, String pURL) {

		final CIMProperty<String> name = new CIMProperty<String>("Name", CIMDataType.STRING_T,
				"JSR48PegasusSampleListener" + getNextId());
		final CIMProperty<String> creationClassName = new CIMProperty<String>("CreationClassName",
				CIMDataType.STRING_T, "CIM_ListenerDestinationCIMXML");
		final CIMProperty<String> destination = new CIMProperty<String>("Destination",
				CIMDataType.STRING_T, pURL);

		final CIMProperty<?>[] properties = new CIMProperty[] { name, creationClassName,
				destination };
		final CIMObjectPath path = new CIMObjectPath(null, null, null, pNamespace,
				"CIM_ListenerDestinationCIMXML", null);

		return new CIMInstance(path, properties);
	}

	/**
	 * Constructs a CIM_IndicationFilter instance
	 * 
	 * @param pNamespace
	 *            The scoping namespace
	 * @param pQuery
	 *            The WQL query of the filter
	 * @return The instance
	 */
	private static CIMInstance makeFilter(String pNamespace, String pQuery) {
		final CIMProperty<String> name = new CIMProperty<String>("Name", CIMDataType.STRING_T,
				"JSR48PegasusSampleFilter" + getNextId());
		final CIMProperty<String> query = new CIMProperty<String>("Query", CIMDataType.STRING_T,
				pQuery);
		final CIMProperty<String> queryLanguage = new CIMProperty<String>("QueryLanguage",
				CIMDataType.STRING_T, "WQL");
		final CIMProperty<String> sourceNameSpace = new CIMProperty<String>("SourceNamespace",
				CIMDataType.STRING_T, pNamespace);

		final CIMProperty<?>[] properties = new CIMProperty[] { name, query, queryLanguage,
				sourceNameSpace };
		final CIMObjectPath path = new CIMObjectPath(null, null, null, pNamespace,
				"CIM_IndicationFilter", null);

		return new CIMInstance(path, properties);
	}

	/**
	 * Constructs a CIM_IndicationSubscription association
	 * 
	 * @param pNamespace
	 *            The scoping namespace
	 * @param pDestinationPath
	 *            The path of the handler
	 * @param pFilterPath
	 *            The path of the filter
	 * @return The association instance
	 */
	private static CIMInstance makeSubscription(String pNamespace, CIMObjectPath pDestinationPath,
			CIMObjectPath pFilterPath) {
		final CIMProperty<CIMObjectPath> handler = new CIMProperty<CIMObjectPath>("Handler",
				new CIMDataType("CIM_ListenerDestinationCIMXML"), pDestinationPath);
		final CIMProperty<CIMObjectPath> filter = new CIMProperty<CIMObjectPath>("Filter",
				new CIMDataType("CIM_IndicationFilter"), pFilterPath);

		final CIMProperty<?>[] properties = new CIMProperty[] { handler, filter };
		final CIMObjectPath path = new CIMObjectPath(null, null, null, pNamespace,
				"CIM_IndicationSubscription", null);

		return new CIMInstance(path, properties);
	}

	/**
	 * Returns a monotonically increasing sequence of integers on subsequent
	 * calls
	 * 
	 * @return An integer
	 */
	private static String getNextId() {
		return String.valueOf(++cId);
	}

	/**
	 * Creates the three CIM instances necessary for making a subscription on
	 * all RT_TestIndication indications in this namespace
	 * 
	 * @param pClient
	 *            The WBEM client to use
	 * @param pNamespace
	 *            The namespace to subscribe in
	 * @return <code>true</code> if the subscription succeeds,
	 *         <code>false</code> otherwise
	 */
	public static boolean subscribe(WBEMClient pClient, String pNamespace) {
		try {

			cDestinationPath = pClient.createInstance(makeListenerDestination(INDICATION_NAMESPACE,
					PROTOCOL + "://" + InetAddress.getLocalHost().getHostAddress() + ":"
							+ LISTENER_PORT + "/create"));
			cFilterPath = pClient.createInstance(makeFilter(INDICATION_NAMESPACE,
					"SELECT * FROM RT_TestIndication"));
			cSubscriptionPath = pClient.createInstance(makeSubscription(pNamespace,
					cDestinationPath, cFilterPath));

			return true;

		} catch (WBEMException e) {
			e.printStackTrace();
		} catch (UnknownHostException e) {
			e.printStackTrace();
		}
		return false;
	}

	/**
	 * Cleans up the instances of the subscription we've made.
	 * 
	 * @param pClient
	 *            The WBEM client to use
	 * @param pNamespace
	 *            The namespace we've subscribed in
	 */
	private static void unsubscribe(WBEMClient pClient, String pNamespace) {
		if (cSubscriptionPath != null) {
			try {
				pClient.deleteInstance(cSubscriptionPath);
			} catch (WBEMException e) {
				e.printStackTrace();
			}
		}
		if (cFilterPath != null) {
			try {
				pClient.deleteInstance(cFilterPath);
			} catch (WBEMException e) {
				e.printStackTrace();
			}
		}
		if (cDestinationPath != null) {
			try {
				pClient.deleteInstance(cDestinationPath);
			} catch (WBEMException e) {
				e.printStackTrace();
			}
		}
	}

	/**
	 * Runs the sample. Will start a listener, subscribe for TestIndication
	 * indication, generate the indication, catch the indication and finally
	 * clean up and shut down.
	 * 
	 * @param args
	 *            A String array containing { CIMOM_URL, USER, PASSWORD } e.g. {
	 *            "http://myserver.mydomain.com:5988", "user", "pw" }
	 */
	static public void main(String[] args) {
		try {
			// Initialize client. This will not trigger any communication with
			// the CIMOM.
			final WBEMClient client = Jsr48OperationSample.connect(new URL(args[0]), args[1],
					args[2]);

			// Namespace where indication provider is registered (see file
			// header)
			final String namespace = PROVIDER_NAMESPACE;

			if (client == null) {
				System.err.println("Client init failed. Probably due to invalid cl parameters.");
				System.err.println("URL: " + args[0]);
				System.err.println("User: " + args[1]);
				System.err.println("Password: " + args[2]);
				return;
			}

			// Start the listener so that we are "on air" when the indication
			// comes in
			if (startListener()) {
				System.out.println("Listener started.");
			} else {
				System.err.println("Listener startup failed. Most probably the port "
						+ LISTENER_PORT + " is not available.");
				client.close();
				return;
			}

			try {
				// Make the subscription. Since this is the first WBEM operation
				// called, the client will connect to the CIMOM now. If we've
				// any connectivity or authentication problems the WBEMException
				// will be thrown right in the subscribe method.
				if (subscribe(client, namespace)) {
					System.out.println("Subscription successful.");
				} else {
					System.err.println("Subscription failed.");
					return;
				}

				// SendTestIndication does not use any in/out parameters
				CIMArgument<?>[] input = new CIMArgument[0];
				CIMArgument<?>[] output = new CIMArgument[0];

				// This will trigger a TestIndication that is caught by our
				// listener
				Object obj = client.invokeMethod(new CIMObjectPath(null, null, null,
						INDICATION_NAMESPACE, "RT_TestIndication", null), "SendTestIndication",
						input, output);

				if (obj.toString().equals("0")) {
					System.out
							.println("Indication generated successfully, waiting for delivery...");
					Thread.sleep(5000);
				} else {
					System.out.println("Indication not generated successfully!");
				}

				System.out.println("Sample completed.");
			} finally {
				// Clean up our subscription
				unsubscribe(client, namespace);
				// Close listener
				cListener.removeListener(Integer.parseInt(LISTENER_PORT));
				client.close();
				System.out.println("Cleaned up.");
			}

		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
