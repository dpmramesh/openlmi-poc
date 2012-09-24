include(UseJava)

set(CMAKE_JAVA_INCLUDE_PATH /usr/share/java/sblim-cim-client2.jar)

set(SRC
    org/curacli/CuraService.java
    org/curacli/CuraPower.java
    org/curacli/CuraUser.java
)

add_jar(CuraCli ${SRC})
