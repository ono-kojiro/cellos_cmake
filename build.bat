<!-- : Begin batch script
@ECHO OFF
@SETLOCAL ENABLEDELAYEDEXPANSION

SET PATH=%SYSTEMROOT%\System32

SET TOP_DIR=%~dp0
ECHO dp0 is !TOP_DIR!
CD /D !TOP_DIR!

ECHO args are %*

SET PATH=C:\msys64\usr\bin;%PATH%

SET PATH=C:\opt\cmake-3.18.4-win64-x64\bin;%PATH%

SET PATH=C:\opt\powerpc-eabi\bin;%PATH%

IF "x%1" == "x" (
	CALL :ALL
	REM disable echo because subroutine might enable echo
	@ECHO OFF
	IF NOT !ERRORLEVEL! == 0 (
		ECHO ERROR : ALL returned !ERRORLEVEL!
		EXIT /B !ERRORLEVEL!
	)
) else (
	FOR %%i IN (%*) DO (
		CALL :_CHECK_LABEL %%i
		IF !ERRORLEVEL! == 0 (
			CALL :%%i %%i
			REM disable echo because subroutine might enable echo
			@ECHO OFF

			IF NOT !ERRORLEVEL! == 0 (
				ECHO ERROR : %%i returned !ERRORLEVEL!
				EXIT /B !ERRORLEVEL!
			)
		) ELSE (
			CALL :_DEFAULT %%i
		)
		
	)
)

@ECHO ON
@EXIT /B !ERRORLEVEL!

REM ===============================
REM === All
REM ===============================
:ALL
ECHO This is all.
bash build.sh %1
@GOTO :EOF

REM ===============================
REM === Config
REM ===============================
:CONFIG
cmake -G "Unix Makefiles" ^
	-D CMAKE_C_COMPILER=powerpc-eabi-gcc ^
	-D CMAKE_AS_COMPILER=powerpc-eabi-as ^
	-D CMAKE_OBJCOPY=powerpc-eabi-objcopy ^
	-D CMAKE_LINKER=powerpc-eabi-ld ^
	.
@GOTO :EOF

REM ===============================
REM === Build
REM ===============================
:BUILD
cmake --build . -- all
@GOTO :EOF

REM ===============================
REM === Clean
REM ===============================
:CLEAN
cmake --build . -- clean
@GOTO :EOF

REM ===============================
REM === MClean
REM ===============================
:MCLEAN
cmake --build . -- clean
cmake -E remove -f CMakeCache.txt
@GOTO :EOF

REM ===============================
REM === Test
REM ===============================
:TEST
ECHO This is test.
CALL sub1.bat
@GOTO :EOF

REM ===============================
REM === Help
REM ===============================
:HELP
cmake --build . -- help
@GOTO :EOF

REM ===============================
REM === _DEFAULT
REM ===============================
:_DEFAULT
ECHO This is default
cmake --build . -- %1
@GOTO :EOF

REM ===============================
REM === _CHECK_LABEL
REM ===============================
:_CHECK_LABEL
FINDSTR /I /R /C:"^[ ]*:%1\>" "%~f0" >NUL 2>NUL
@GOTO :EOF

----- Begin wsf script --->
<package>
	<job id="Main">
		<?job debug="true"?>
		<script language="JavaScript">
			WScript.Echo("Hello JavaScript World");
			WScript.Quit(1);
		</script>
	</job>

	<job id="Clean">
		<?job debug="true"?>
		<script language="JavaScript">
			WScript.Echo("This is clean job");
			WScript.Quit(1);
		</script>
	</job>
</package>

