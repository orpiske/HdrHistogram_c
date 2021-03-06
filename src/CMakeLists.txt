FILE(GLOB histogram_files "*.c")
FILE(GLOB HEADER "*.h")

add_library(hdr_histogram SHARED ${histogram_files} ${HEADER})
add_library(hdr_histogram_static STATIC ${histogram_files} ${HEADER})


if(WIN32)
    target_link_libraries(hdr_histogram ${ZLIB_LIBRARIES})
    target_link_libraries(hdr_histogram_static ${ZLIB_LIBRARIES})
else()
    target_link_libraries(hdr_histogram m z)
    target_link_libraries(hdr_histogram_static m z)
endif()

if (WIN32)
    set_target_properties(hdr_histogram PROPERTIES VERSION ${HDR_VERSION})
else (WIN32)
    set_target_properties(hdr_histogram PROPERTIES VERSION ${HDR_VERSION} SOVERSION ${HDR_SOVERSION})
endif (WIN32)

target_include_directories(hdr_histogram SYSTEM PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
target_include_directories(hdr_histogram_static SYSTEM PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

install(TARGETS hdr_histogram DESTINATION lib${LIB_SUFFIX})
install(TARGETS hdr_histogram_static DESTINATION lib${LIB_SUFFIX})
install(FILES hdr_histogram.h hdr_histogram_log.h hdr_time.h hdr_writer_reader_phaser.h hdr_interval_recorder.h hdr_thread.h DESTINATION include/hdr)
