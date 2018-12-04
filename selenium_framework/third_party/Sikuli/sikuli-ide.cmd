@echo off
SETLOCAL

if "%1"=="-h" (
  echo +++ usage of sikuli-ide.cmd
  echo     [] = default
  echo     JRE 7 is used if present 
  echo -j6 assure to use JRE6 if JRE7 is present
  echo d:n set debug level to n [1]
  echo -f  logs to SikuliLog.txt in working dir
  echo -u  user logs go to UserLog.txt in working dir
  echo -c  all output goes to command window synchonously [IDE message area]
  echo.
  echo if you want to store something in sys.argv for later script runs
  echo --  ends the command script option list - trailing stuff goes to sys.argv
  goto FINALLY
)

IF "%SIKULIX_HOME%"=="" set SIKULIX_HOME=%~dp0
set PARMS=-Xms64M -Xmx512M -Dfile.encoding=UTF-8

for %%p in ( %* ) do (
if defined PSTOP goto LOOPCONT
if "%%~dp"=="D:" set DEBUG=-Dsikuli.Debug=%%~np
if "%%p"=="-j6" set J6=YES
if "%%p"=="-f" set LOGFILE=-Dsikuli.Logfile
if "%%p"=="-u" set USERLOG=-Dsikuli.LogfileUser
if "%%p"=="-c" set CONSOLE=-Dsikuli.console=false
:LOOPCONT
if "%%p"=="--" set PSTOP=YES
)

for %%p in ( %* ) do (
if defined PSTOP1 goto LOOPCONT1
shift
:LOOPCONT1
if "%%p"=="--" set PSTOP1=YES
)

set PARMS=%PARMS% %DEBUG% %LOGFILE% %USERLOG% %CONSOLE%
echo %PARMS%
set SPARMS=%1 %2 %3 %4 %5 %6 %7 %8 %9
echo %SPARMS%

rem goto FINALLY

echo +++ using as SIKULIX_HOME: %SIKULIX_HOME%
IF NOT EXIST "%SIKULIX_HOME%libs" (
  echo +++ SIKULIX_HOME seems to be invalid
  GOTO STOPIT
)

set PROGRAMS=%ProgramFiles%
if not exist "%SIKULIX_HOME%libs\MadeForWindows32Bit.txt" goto ARCHXX
echo +++ this Sikuli version is 32-Bit
if defined ProgramFiles(x86) set PROGRAMS=%ProgramFiles(x86)%
goto ARCHOK
:ARCHXX
if exist "%SIKULIX_HOME%libs/MadeForWindows64Bit.txt" goto ARCH64
  echo SIKULIX_HOME not found or seems to be invalid \( $SIKULIX_HOME \)
  set SIKULIX_HOME=INVALID 
  echo giving up
  goto STOPIT
:ARCH64
echo +++ this Sikuli version is 64-Bit

:ARCHOK
set JAVA6=%PROGRAMS%\Java\jre6\bin
set JAVA7=%PROGRAMS%\Java\jre7\bin

if defined J6 goto JAVA6

IF not EXIST "%JAVA7%" goto JAVA6
set JAVA=%JAVA7%
goto JAVA_OK

:JAVA6
IF not EXIST "%JAVA6%" goto JAVANO
set JAVA=%JAVA6%
goto JAVA_OK

:JAVANO
echo +++ Java not found
goto STOPIT

:JAVA_OK 
PATH=%SIKULIX_HOME%libs;%JAVA%;%PATH%
echo +++ trying to start Sikuli IDE with %JAVA%
"%JAVA%\java.exe" %PARMS% %SIKULI_PARMS% -jar "%SIKULIX_HOME%sikuli-ide.jar" %SPARMS% %SIKULI_USERPARMS%
GOTO FINALLY

:STOPIT
echo.+++ ended with some errors
:FINALLY
ENDLOCAL