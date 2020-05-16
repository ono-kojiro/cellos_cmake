project(cellos LANGUAGES C ASM)

set(LINKERSCRIPT ${CMAKE_CURRENT_SOURCE_DIR}/cellos.lds)

set(CMAKE_C_LINK_FLAGS "-g")
set(CMAKE_C_LINK_FLAGS "${CMAKE_C_LINK_FLAGS} -O2")
set(CMAKE_C_LINK_FLAGS "${CMAKE_C_LINK_FLAGS} --script=${LINKERSCRIPT}")
set(CMAKE_C_LINK_FLAGS "${CMAKE_C_LINK_FLAGS} -Ttext 0x0")

set(CMAKE_ASM_COMPILE_OBJECT "<CMAKE_ASM_COMPILER> <DEFINES> <INCLUDES> <FLAGS> -o <OBJECT> -c <SOURCE>")
set(CMAKE_ASM_LINK_EXECUTABLE "<CMAKE_LINKER> <LINK_FLAGS> <OBJECTS> -o <TAR    GET> <LINK_LIBRARIES>")

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
	PUBLIC -O2
	PUBLIC -fno-exceptions
	PUBLIC -fno-builtin
	PUBLIC -msoft-float
	PUBLIC $<$<COMPILE_LANGUAGE:ASM>:-Xassembler>
	PUBLIC $<$<COMPILE_LANGUAGE:ASM>:-m405>
	PUBLIC $<$<COMPILE_LANGUAGE:ASM>:-mregnames>
)

