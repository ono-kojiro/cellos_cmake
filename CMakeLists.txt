cmake_minimum_required(VERSION 3.11)

cmake_policy(SET CMP0048 NEW)
#cmake_policy(SET CMP0076 OLD)

#
# enable recursive target for custom target
# 
#cmake_policy(SET CMP0002 OLD)
#set_property(GLOBAL PROPERTY ALLOW_DUPLICTE_CUSTOM_TARGET ON)


set(CMAKE_DISABLE_IN_SOURCE_BUILD ON)
#if("${CMAKE_SOURCE_DIR}" STREQUAL "${CMAKE_BINARY_DIR}")
#   message("CMAKE_SOURCE_DIR is ${CMAKE_SOURCE_DIR}")
#   message("CMAKE_BINARY_DIR is ${CMAKE_BINARY_DIR}")
#   message(FATAL_ERROR "In-source builds are not allowed.")
#endif("${CMAKE_SOURCE_DIR}" STREQUAL "${CMAKE_BINARY_DIR}")

set(CMAKE_SYSTEM_NAME Generic)

project(cellos_cmake)
set(PROJECT_VERSION 1.0.0)

set(CMAKE_BUILD_TYPE Debug)

set(CMAKE_COLOR_MAKEFILE OFF)
set(CMAKE_VERBOSE_MAKEFILE ON)

find_program(CC powerpc-eabi-gcc)
find_program(AS powerpc-eabi-as)
find_program(LD powerpc-eabi-ld)

set(CMAKE_C_COMPILER ${CC} CACHE string "powerpc-eabi-gcc" FORCE)
set(CMAKE_AS_COMPILER ${AS} CACHE string "powerpc-eabi-as" FORCE)
set(CMAKE_LINKER ${LD} CACHE string "powerpc-eabi-ld" FORCE)

set(CMAKE_C_LINK_EXECUTABLE "<CMAKE_LINKER> <CMAKE_C_LINK_FLAGS> -o <TARGET> <LINK_FLAGS> <OBJECTS> <LINK_LIBRARIES>")
set(CMAKE_AS_LINK_EXECUTABLE "<CMAKE_LINKER> <CMAKE_C_LINK_FLAGS> -o <TARGET> <LINK_FLAGS> <OBJECTS> <LINK_LIBRARIES>")

set(CELLOS_ROOT ${CMAKE_SOURCE_DIR}/src)

add_subdirectory(driver ${CMAKE_CURRENT_BINARY_DIR}/driver)
add_subdirectory(kernel ${CMAKE_CURRENT_BINARY_DIR}/kernel)
add_subdirectory(cellos ${CMAKE_CURRENT_BINARY_DIR}/cellos)
add_subdirectory(startup ${CMAKE_CURRENT_BINARY_DIR}/startup)
add_subdirectory(bootrom ${CMAKE_CURRENT_BINARY_DIR}/bootrom)

# 'make package' creates tar.bz2 binary package
#set(CPACK_GENERATOR "TBZ2")
set(CPACK_GENERATOR "TGZ")
set(CPACK_PACKAGE_FILE_NAME "${CMAKE_PROJECT_NAME}-${PROJECT_VERSION}-bin")

# 'make package_source' create source package
set(CPACK_SOURCE_GENERATOR "TGZ")
set(CPACK_OUTPUT_FILE_PREFIX "..")
set(CPACK_SOURCE_PACKAGE_FILE_NAME "${CMAKE_PROJECT_NAME}-${PROJECT_VERSION}")
set(CPACK_SOURCE_IGNORE_FILES "/.git/;/.svn/;${CPACK_SOURCE_IGNORE_FILES}")
include(CPack)

#get_cmake_property(_variableNames VARIABLES)
#list (SORT _variableNames)
#foreach (_variableName ${_variableNames})
#	message(STATUS "${_variableName}=${${_variableName}}")
#endforeach()

