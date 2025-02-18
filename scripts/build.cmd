@echo off
set SRC_FILE=%1
set RUN=%2

if "%SRC_FILE%"=="" (
    echo Please provide C++ file to compile
    echo Usage: build.bat ^<filename.cpp^>
    exit /b 1
)

set OUTPUT_FILE=%~dp1%~n1.exe

set CXX=g++
set CXXFLAGS=-O2 -Wall -Wextra -std=c++20 -static-libgcc -static-libstdc++ -pedantic -Wshadow -Wformat=2 -Wfloat-equal -Wconversion -Wlogical-op -Wshift-overflow=2 -Wduplicated-cond -Wcast-qual -Wcast-align -D_GLIBCXX_DEBUG -fmax-errors=1 -Winvalid-pch -mconsole -DDEBUG -I"D:\3.Personal\CompetitiveProgramming\template"

echo Compiling %SRC_FILE% ...

"%CXX%" %CXXFLAGS% "%SRC_FILE%" -o "%OUTPUT_FILE%"

:: Check for success or failure
if %ERRORLEVEL%==0 (
    echo Compilation successful!
    if "%RUN%"=="1" (
        echo -------------------------------------------
        "%OUTPUT_FILE%"
    )
) else (
    echo Compilation failed!
)
