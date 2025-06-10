@echo off
set SRC_FILE=%1
set RUN=%2

if "%SRC_FILE%"=="" (
    echo Please provide Kotlin file to compile
    echo Usage: build_kotlin.bat ^<filename.kt^>
    exit /b 1
)

set "FILENAME=%~n1%"
set "JAR_FILE=%~dp1%FILENAME%.jar"

echo Compiling %SRC_FILE% ...

kotlinc %SRC_FILE% -include-runtime -d "%JAR_FILE%"

:: Check for success or failure
if %ERRORLEVEL%==0 (
    echo Compilation successful!
    if "%RUN%"=="1" (
        echo -------------------------------------------
        java -jar "%JAR_FILE%"
    )
    exit /b 0
) else (
    echo Compilation failed!
    exit /b 1
)
