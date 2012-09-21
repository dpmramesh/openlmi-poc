cmake_minimum_required(VERSION 2.8.6)
project(java_client Java)

find_package(Java)
include(UseJava)

set(CMAKE_VERBOSE_MAKEFILE 1)
set(CMAKE_JAVA_INCLUDE_PATH /usr/share/java/sblim-cim-client2.jar)
#set(CMAKE_JAVA_MANIFEST src/javaclient.mf)

set(SRC
    src/JavaClient.java
)

add_jar(JavaClient ${SRC})
