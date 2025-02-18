@echo off
setlocal

:: Add scripts directory to user PATH
set "SCRIPT_DIR=%~dp0"
for /f "tokens=2*" %%a in ('reg query "HKCU\Environment" /v PATH') do set "USER_PATH=%%b"
setx PATH "%SCRIPT_DIR%;%USER_PATH%"

echo Scripts directory added to PATH
echo Please restart your command prompt for changes to take effect 