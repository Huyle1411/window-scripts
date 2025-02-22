@echo off
setlocal

:: Add scripts directory to user PATH
set "SCRIPT_DIR=%~dp0"
:: Remove trailing backslash from SCRIPT_DIR
set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"
set "PROJECT_ROOT=%SCRIPT_DIR%\.."

:: Convert to absolute path
pushd "%PROJECT_ROOT%"
set "PROJECT_ROOT=%CD%"
popd

:: Set up PATH
for /f "tokens=2*" %%a in ('reg query "HKCU\Environment" /v PATH') do set "USER_PATH=%%b"
setx PATH "%SCRIPT_DIR%;%USER_PATH%"

:: Set up CP_TOOL_ROOT
setx CP_TOOL_ROOT "%PROJECT_ROOT%"

echo Scripts directory added to PATH: %SCRIPT_DIR%
echo CP_TOOL_ROOT set to: %PROJECT_ROOT%
echo Please restart your command prompt for changes to take effect

endlocal 