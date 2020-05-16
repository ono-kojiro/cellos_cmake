project(cellos LANGUAGES C ASM)

set(CELLOS_ROOT ${CMAKE_SOURCE_DIR}/../cellos)

#set(LINKERSCRIPT ${CELLOS_ROOT}/src/arch/ppc32/ppc405/cellos.lds)
set(LINKERSCRIPT ${CMAKE_CURRENT_SOURCE_DIR}/cellos.lds)

set(CMAKE_C_LINK_FLAGS "-g")
set(CMAKE_C_LINK_FLAGS "${CMAKE_C_LINK_FLAGS} -O2")
set(CMAKE_C_LINK_FLAGS "${CMAKE_C_LINK_FLAGS} --script=${LINKERSCRIPT}")
set(CMAKE_C_LINK_FLAGS "${CMAKE_C_LINK_FLAGS} -Ttext 0x0")

set(CMAKE_ASM_COMPILE_OBJECT "<CMAKE_ASM_COMPILER> <DEFINES> <INCLUDES> <FLAGS> -o <OBJECT> -c <SOURCE>")
set(CMAKE_ASM_LINK_EXECUTABLE "<CMAKE_LINKER> <LINK_FLAGS> <OBJECTS> -o <TAR    GET> <LINK_LIBRARIES>")

add_library(${PROJECT_NAME}
	${CELLOS_ROOT}/src/lib/cpu.c
	${CELLOS_ROOT}/src/lib/ctype.c
	${CELLOS_ROOT}/src/lib/extable.c
	${CELLOS_ROOT}/src/lib/interrupts.c
	${CELLOS_ROOT}/src/lib/malloc.c
	${CELLOS_ROOT}/src/lib/speed.c
	${CELLOS_ROOT}/src/lib/string.c
	${CELLOS_ROOT}/src/lib/time.c
	${CELLOS_ROOT}/src/lib/traps.c
	${CELLOS_ROOT}/src/lib/uic.c
	${CELLOS_ROOT}/src/lib/vsprintf.c
	${CELLOS_ROOT}/src/lib/cache.S
	${CELLOS_ROOT}/src/lib/dcr.S
	${CELLOS_ROOT}/src/lib/ppccache.S
	${CELLOS_ROOT}/src/lib/ppcstring.S
	${CELLOS_ROOT}/src/lib/ticks.S
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

