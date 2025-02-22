@echo off
set SRC_FILE=%1
set RUN=%2

if "%SRC_FILE%"=="" (
    echo Please provide Java file to compile
    echo Usage: build.bat ^<filename.java^>
    exit /b 1
)

set "FILENAME=%~n1%"

echo Compiling %SRC_FILE% ...

javac -Xlint:all -g -encoding UTF-8 %SRC_FILE%

:: Check for success or failure
if %ERRORLEVEL%==0 (
    echo Compilation successful!
    if "%RUN%"=="1" (
        echo -------------------------------------------
        java %FILENAME%
    )
    exit /b 0
) else (
    echo Compilation failed!
    exit /b 1
)
