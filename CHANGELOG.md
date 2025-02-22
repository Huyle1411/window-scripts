# Changelog

All notable changes to this project will be documented in this file.

## [2.2.2] - 2025-02-22
### Changed
- Updated `config.py` to use `CP_TOOL_ROOT` environment variable 


## [2.2.1] - 2025-02-22

### Changed
- Make template path relative to project root instead of using absolute path
- Improved build scripts error handling and environment setup:
  - Added proper error code returns in build.cmd and build_java.cmd
  - Fixed CP_TOOL_ROOT environment variable setup in setup.cmd
  - Made template include path use CP_TOOL_ROOT instead of hardcoded path
- Improved logging system:
  - Added date-based log files (log_YYYY-MM-DD.txt)
  - Created logs directory automatically if not exists
  - Moved logs to project-level logs directory


## [2.2.0] - 2025-02-18

### Changed
- Simplified project structure by removing package installation requirement
- Removed ProblemData class in favor of direct JSON handling
- Changed logging to write to log.txt file
- Fixed command argument handling in cptool.cmd

### Added
- Basic .gitignore file for Python cache
- Individual command scripts (dl.cmd, run.cmd, test.cmd)

### Fixed
- Fixed version display in CLI
- Fixed relative import issues
- Fixed argument passing in command scripts

## [2.1.0] - 2024-02-17

### Changed
- Restructured project into proper Python package
- Renamed main command from `cp` to `cptool` to avoid conflicts
- Moved all Python code under `src/cp_tool/`
- Organized core functionality into separate modules
- Moved all scripts to `scripts/` directory

### Added
- Better project documentation
- Clearer command structure
- Proper Python package configuration

## [2.0.0] - 2024-03-20

### Added
- Refactored code into classes
- Added type hints
- Improved error handling

### Changed
- Moved configuration to separate file
- Improved file path handling using pathlib

### Fixed
- Fixed inconsistent file path separators
- Improved error messages

## [1.0.0] - 2024-01-01

### Added
- Initial release
- Basic test case download functionality
- Support for running and testing solutions 