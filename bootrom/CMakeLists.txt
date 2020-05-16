project(bootrom LANGUAGES C ASM)

set(CMAKE_LINKER "powerpc-eabi-ld")

set(CELLOS_ROOT ${CMAKE_SOURCE_DIR}/../cellos)

set(LINKERSCRIPT ${CMAKE_CURRENT_SOURCE_DIR}/linkerscript.ld)

set(CMAKE_ASM_COMPILER ${AS})
set(CMAKE_LINKER ${LD})

set(CMAKE_ASM_COMPILE_OBJECT "<CMAKE_ASM_COMPILER> -o <OBJECT> <SOURCE>")
set(CMAKE_ASM_LINK_EXECUTABLE "<CMAKE_LINKER> <LINK_FLAGS> <OBJECTS> -o <TARGET> <LINK_LIBRARIES>")

add_executable(${PROJECT_NAME}
	${CELLOS_ROOT}/src/arch/ppc32/ppc405/boot/bootrom.S
)

#target_compile_definitions(${PROJECT_NAME}
#	PUBLIC $<$<COMPILE_LANGUAGE:C>:__KERNEL__>
#	PUBLIC $<$<COMPILE_LANGUAGE:ASM>:__ASSEMBLY__>
#)

#target_compile_definitions(${PROJECT_NAME} PUBLIC -DTEXT_BASE=0x0)

#target_include_directories(${PROJECT_NAME}
#    PUBLIC ${CELLOS_ROOT}/src/arch/ppc32/ppc405/include
#)

target_link_libraries(${PROJECT_NAME}
	PUBLIC --script=${LINKERSCRIPT}
)

set_target_properties(${PROJECT_NAME} PROPERTIES OUTPUT_NAME "bootrom.elf")

add_custom_command(TARGET ${PROJECT_NAME}
	POST_BUILD
	COMMAND powerpc-eabi-objcopy -O binary bootrom.elf ppc405_rom.bin
)


