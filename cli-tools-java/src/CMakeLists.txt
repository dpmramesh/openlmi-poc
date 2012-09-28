include(UseJava)

set(CMAKE_JAVA_INCLUDE_PATH /usr/share/java/sblim-cim-client2.jar:/usr/share/java/args4j.jar)

set(SRC
    org/cura/curaoptions/CuraBasicOptions.java
    org/cura/curaservice/CuraService.java
    org/cura/curaservice/CuraServiceClient.java
    org/cura/curapower/CuraPower.java
    org/cura/curapower/CuraPowerClient.java
)

add_jar(CuraCli ${SRC})
