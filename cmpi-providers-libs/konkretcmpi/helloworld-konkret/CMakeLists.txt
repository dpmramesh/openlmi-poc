
cmake_minimum_required(VERSION 2.6)

# Set flags and definitions
add_definitions(-D_XOPEN_SOURCE=500 -D_GNU_SOURCE)
set(CMAKE_C_FLAGS "-std=c99 -Wall -pedantic -g -Wextra -Wno-unused-parameter -Wformat -Wparentheses -Wl,--no-undefined")

# Set LIB_SUFFIX to 64 on 64bit architectures
if(CMAKE_SIZEOF_VOID_P EQUAL 4)
    set(LIB_SUFFIX "")
else(CMAKE_SIZEOF_VOID_P EQUAL 4)
    SET(LIB_SUFFIX 64)
endif(CMAKE_SIZEOF_VOID_P EQUAL 4)

option(WITH-FAN "Build fan provider" ON)
option(WITH-POWER "Build power provider" ON)
option(WITH-SERVICE "Build service provider" ON)
option(WITH-ACCOUNT "Build account provider" ON)

# Set path to custom cmake modules
set(CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake/modules ${CMAKE_MODULE_PATH})

include(CuraMacros)

find_package(PkgConfig)

# Find required packages
find_package(CMPI REQUIRED)
find_package(KonkretCMPI REQUIRED)

add_subdirectory(src)
add_subdirectory(mof)
add_subdirectory(cli-tools)

install(PROGRAMS register.sh reg2pegasus.py DESTINATION share/cura-providers)
install(FILES cmake/modules/CuraMacros.cmake DESTINATION share/cmake/Modules)
install(FILES cmake/modules/FindCMPI.cmake DESTINATION share/cmake/Modules)
install(FILES cmake/modules/FindKonkretCMPI.cmake DESTINATION share/cmake/Modules)
