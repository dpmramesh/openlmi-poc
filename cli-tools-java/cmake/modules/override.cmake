# http://www.cmake.org/Bug/view.php?id=7832

# compile a Java file into an object file
FILE(MAKE_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}/.class")

SET(CMAKE_Java_COMPILE_OBJECT
  "<CMAKE_Java_COMPILER> <FLAGS> <SOURCE> -d \"<CMAKE_CURRENT_BINARY_DIR>/.class\""
)

# this is a place holder if java needed flags for javac they would go here.
SET(CMAKE_Java_CREATE_STATIC_LIBRARY
  "<CMAKE_Java_ARCHIVE> -cf <TARGET> -C \"<CMAKE_CURRENT_BINARY_DIR>/.class\" ."
)
