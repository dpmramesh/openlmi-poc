cmake_minimum_required(VERSION 2.8.6)
project(cli_java_tools Java)

find_package(Java)

# set path to custom cmake modules
set(CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake/modules ${CMAKE_MODULE_PATH})
set(CMAKE_VERBOSE_MAKEFILE 1)

# Java stuff we have overridden (located in cmake/modules/override.cmake)
SET(CMAKE_USER_MAKE_RULES_OVERRIDE "override")

ADD_SUBDIRECTORY(src)

