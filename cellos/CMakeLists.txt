

project(cellos LANGUAGES C ASM)

# change asm compiler temporarily 
set(CMAKE_ASM_COMPILER ${CC})

add_library(${PROJECT_NAME}
	${CELLOS_ROOT}/lib/cpu.c
	${CELLOS_ROOT}/lib/ctype.c
	${CELLOS_ROOT}/lib/extable.c
	${CELLOS_ROOT}/lib/interrupts.c
	${CELLOS_ROOT}/lib/malloc.c
	${CELLOS_ROOT}/lib/speed.c
	${CELLOS_ROOT}/lib/string.c
	${CELLOS_ROOT}/lib/time.c
	${CELLOS_ROOT}/lib/traps.c
	${CELLOS_ROOT}/lib/uic.c
	${CELLOS_ROOT}/lib/vsprintf.c
	${CELLOS_ROOT}/lib/cache.S
	${CELLOS_ROOT}/lib/dcr.S
	${CELLOS_ROOT}/lib/ppccache.S
	${CELLOS_ROOT}/lib/ppcstring.S
	${CELLOS_ROOT}/lib/ticks.S
)

target_compile_definitions(${PROJECT_NAME}
	PUBLIC $<$<COMPILE_LANGUAGE:C>:__KERNEL__>
	PUBLIC TEXT_BASE=0x0
	PUBLIC $<$<COMPILE_LANGUAGE:ASM>:__ASSEMBLY__>
)

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
	PUBLIC $<$<COMPILE_LANGUAGE:C>:-O2>
	PUBLIC -fno-exceptions
	PUBLIC -fno-builtin
	PUBLIC -msoft-float
	PUBLIC $<$<COMPILE_LANGUAGE:ASM>:-Xassembler>
	PUBLIC $<$<COMPILE_LANGUAGE:ASM>:-m405>
	PUBLIC $<$<COMPILE_LANGUAGE:ASM>:-mregnames>
)

