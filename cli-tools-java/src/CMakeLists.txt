include(UseJava)

set(CMAKE_JAVA_INCLUDE_PATH /usr/share/java/sblim-cim-client2.jar:/usr/share/java/args4j.jar)

set(SRC
    org/cura/curaoptions/CuraBasicOptions.java
    org/cura/curaservice/CuraService.java
    org/cura/curapower/CuraPower.java
    org/cura/curauser/CuraUser.java
)

add_jar(CuraCli ${SRC})
