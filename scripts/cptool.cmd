@echo off
setlocal

:: Set the path to the scripts directory
set SCRIPT_DIR=D:\3.Personal\CompetitiveProgramming\scripts

:: Get the command from the first argument
set COMMAND=%1
shift

:: Map commands to their respective Python scripts
if /i "%COMMAND%"=="dl" (
    set PYTHON_SCRIPT=%SCRIPT_DIR%\core\downloader.py
) else if /i "%COMMAND%"=="run" (
    set PYTHON_SCRIPT=%SCRIPT_DIR%\core\runner.py
) else (
    echo Unknown command: %COMMAND%
    echo Usage: cptool dl [args] or cptool run [args]
    exit /b 1
)

:: Run the script with remaining arguments
python "%PYTHON_SCRIPT%" %*

:: Preserve the exit code from the Python script
exit /b %ERRORLEVEL% 