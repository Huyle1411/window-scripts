@echo off
setlocal

:: Set the path to the scripts directory
set SCRIPT_DIR=%~dp0..\src\cp_tool\core

:: Get the command from the first argument
set COMMAND=%1

:: Remove first argument and keep the rest
set ARGS=%2
:loop
shift
if [%2]==[] goto continue
set ARGS=%ARGS% %2
goto loop
:continue

:: Map commands to their respective Python scripts
if /i "%COMMAND%"=="dl" (
    python "%SCRIPT_DIR%\downloader.py" %ARGS%
) else if /i "%COMMAND%"=="run" (
    python "%SCRIPT_DIR%\runner.py" %ARGS%
) else if /i "%COMMAND%"=="test" (
    python "%SCRIPT_DIR%\tester.py" %ARGS%
) else (
    echo Unknown command: %COMMAND%
    echo Usage: cptool ^<command^> [args]
    echo Commands:
    echo   dl    - Download test cases
    echo   run   - Run solution
    echo   test  - Test solution
    exit /b 1
)

:: Preserve the exit code from the Python script
exit /b %ERRORLEVEL%