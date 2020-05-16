project(kernel LANGUAGES C)

set(CELLOS_ROOT ${CMAKE_SOURCE_DIR}/../cellos)

add_library(${PROJECT_NAME}
	${CELLOS_ROOT}/src/kernel/cellSched.c
	${CELLOS_ROOT}/src/kernel/cellMain.c
)


target_compile_definitions(${PROJECT_NAME}
	PUBLIC $<$<COMPILE_LANGUAGE:C>:__KERNEL__>
	PUBLIC $<$<COMPILE_LANGUAGE:ASM>:__ASSEMBLY__>
)

target_compile_definitions(${PROJECT_NAME} PUBLIC -DTEXT_BASE=0x0)

target_include_directories(${PROJECT_NAME}
    PUBLIC ${CELLOS_ROOT}/src/arch/ppc32/ppc405/include
    PUBLIC ${CELLOS_ROOT}/src/arch/ppc32/ppc405
    PUBLIC ${CELLOS_ROOT}/src/arch/ppc32/ppc405/platforms/taihu
    PUBLIC ${CELLOS_ROOT}/src/include
    PUBLIC ${CELLOS_ROOT}/src/kernel
    PUBLIC ${CELLOS_ROOT}/src/lib
    PUBLIC ${CELLOS_ROOT}/src/drivers
    PUBLIC ${CELLOS_ROOT}/src/drivers/serial
    PUBLIC ${CELLOS_ROOT}/src/tools
)

target_compile_options(${PROJECT_NAME}
	PUBLIC -Wall
	PUBLIC -g
	PUBLIC -O2
	PUBLIC -fno-exceptions
	PUBLIC -fno-builtin
	PUBLIC -msoft-float
	PUBLIC $<$<COMPILE_LANGUAGE:ASM>:-Xassembler>
	PUBLIC $<$<COMPILE_LANGUAGE:ASM>:-m405>
	PUBLIC $<$<COMPILE_LANGUAGE:ASM>:-mregnames>
)

