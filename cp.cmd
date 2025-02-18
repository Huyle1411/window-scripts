@echo off
setlocal

:: Set the path to the scripts directory
set SCRIPT_DIR=D:\3.Personal\CompetitiveProgramming\scripts

:: Get the command from the first argument
set COMMAND=%1
shift

:: Map commands to their respective Python scripts
if /i "%COMMAND%"=="dl" (
    set PYTHON_SCRIPT=%SCRIPT_DIR%\download_tc.py
) else if /i "%COMMAND%"=="run" (
    set PYTHON_SCRIPT=%SCRIPT_DIR%\run.py
) else (
    echo Unknown command: %COMMAND%
    echo Usage: cp dl [args] or cp run [args]
    exit /b 1
)

:: Check if Python is available
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Python is not found in PATH
    exit /b 1
)

:: Check if the script exists
if not exist "%PYTHON_SCRIPT%" (
    echo Script not found: %PYTHON_SCRIPT%
    exit /b 1
)

:: Run the script with remaining arguments
python "%PYTHON_SCRIPT%" %*

:: Preserve the exit code from the Python script
exit /b %ERRORLEVEL% 