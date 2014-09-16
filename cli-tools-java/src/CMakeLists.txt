include(UseJava)

set(CMAKE_JAVA_INCLUDE_PATH /usr/share/java/sblim-cim-client2.jar:/usr/share/java/args4j.jar)

set(SRC
    org/openlmi/openlmioptions/OpenLMIBasicOptions.java
    org/openlmi/openlmiservice/OpenLMIService.java
    org/openlmi/openlmiservice/OpenLMIServiceClient.java
    org/openlmi/openlmipower/OpenLMIPower.java
    org/openlmi/openlmipower/OpenLMIPowerClient.java
    org/openlmi/openlmistorage/OpenLMIStorageClient.java
    org/openlmi/openlmistorage/OpenLMIStorage.java
)

add_jar(OpenLMICli ${SRC})
