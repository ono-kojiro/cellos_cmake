project(driver LANGUAGES C)

add_library(${PROJECT_NAME}
	${CELLOS_ROOT}/drivers/serial/ppc4xxSerial.c
)

target_compile_definitions(${PROJECT_NAME}
	PUBLIC $<$<COMPILE_LANGUAGE:C>:__KERNEL__>
	PUBLIC $<$<COMPILE_LANGUAGE:ASM>:__ASSEMBLY__>
)

target_compile_definitions(${PROJECT_NAME} PUBLIC -DTEXT_BASE=0x0)

target_include_directories(${PROJECT_NAME}
    PUBLIC ${CELLOS_ROOT}/arch/ppc32/ppc405/include
    PUBLIC ${CELLOS_ROOT}/arch/ppc32/ppc405
    PUBLIC ${CELLOS_ROOT}/arch/ppc32/ppc405/platforms/taihu
    PUBLIC ${CELLOS_ROOT}/include
    PUBLIC ${CELLOS_ROOT}/kernel
    PUBLIC ${CELLOS_ROOT}/lib
    PUBLIC ${CELLOS_ROOT}/drivers
    PUBLIC ${CELLOS_ROOT}/drivers/serial
    PUBLIC ${CELLOS_ROOT}/tools
)

target_compile_options(${PROJECT_NAME}
	PUBLIC -Wall
	PUBLIC -g
	PUBLIC -fno-exceptions
	PUBLIC -fno-builtin
	PUBLIC -msoft-float
	PUBLIC $<$<COMPILE_LANGUAGE:ASM>:-Xassembler>
	PUBLIC $<$<COMPILE_LANGUAGE:ASM>:-m405>
	PUBLIC $<$<COMPILE_LANGUAGE:ASM>:-mregnames>
)

set_source_files_properties(
	${CELLOS_ROOT}/drivers/serial/ppc4xxSerial.c
	APPEND PROPERTY COMPILE_FLAGS "-Os -O2"
)

#add_custom_command(TARGET ${PROJECT_NAME}
#	POST_BUILD
#	COMMAND powerpc-eabi-objcopy -O binary libdriver.a
#)

#set_directory_properties(
#	PROPERTIES ADDITIONAL_MAKE_CLEAN_FILES libdriver.bin
#)

