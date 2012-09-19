include_directories(${CMAKE_CURRENT_SOURCE_DIR})

set(PROVIDER_NAME Widget)
set(LIBRARY_NAME cmpiWidget_${PROVIDER_NAME})
set(MOF Widget.mof)

set_target_properties(PROPERTIES SOVERSION 0.0.1)

set(provider_SRCS
	WidgetProvider.c
)

#konkretcmpi_generate(${MOF}
#                     CIM_PROVIDERS
#                     CIM_HEADERS
#)

add_library(${LIBRARY_NAME} SHARED
            ${provider_SRCS}
            ${CIM_PROVIDERS}
            ${CIM_HEADERS}
)

include_directories(${CMAKE_CURRENT_BINARY_DIR} ${CMPI_INCLUDE_DIR})
target_link_libraries(${LIBRARY_NAME} curacommon ${KONKRETCMPI_LIBRARIES})

# Create registration file
#cim_registration(${PROVIDER_NAME} ${LIBRARY_NAME} ${MOF} share/cura-providers)

