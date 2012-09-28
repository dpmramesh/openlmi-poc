include_directories(.)

add_library(curacommon SHARED
            globals.c
)

set_target_properties(curacommon PROPERTIES SOVERSION 0.0.1)

install(TARGETS curacommon DESTINATION lib${LIB_SUFFIX})
install(FILES globals.h DESTINATION include/cura)

if (WITH-FAN)
    add_subdirectory(fan)
endif (WITH-FAN)

if (WITH-POWER)
    add_subdirectory(power)
endif (WITH-POWER)

if (WITH-SERVICE)
    add_subdirectory(service)
endif (WITH-SERVICE)

if (WITH-ACCOUNT)
    add_subdirectory(account)
endif (WITH-ACCOUNT)
