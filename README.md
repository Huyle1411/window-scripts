# Competitive Programming Tool

A command-line tool to help with competitive programming tasks.

## Installation

1. Clone this repository
2. Run `scripts/setup.cmd` to add the scripts directory to your PATH
3. Restart your command prompt for changes to take effect

## Project Structure

**Set PATH in environment variables to run script globally**

## Commands

- Compile/run C++ file. If `is_run == 1`, run after compile successful  
`build <filename.cpp> <is_run: optional>`

- Show help information.
`cptool -h`

- Show version.of downloader.
`cptool dl -v` or `dl -v`

- Download sample test cases, make folder problem, ... For more information, run:  
`cptool dl -h` or `dl -h`

- Test solution with sample test cases, support C++/Python/Java. If `is_debug_mode != 0`, always print input, actual_output and expected_output. Otherwise, only print input and output in case of wrong answer.
`cptool test <problem_folder_name> <language:cpp or py or java> <is_debug_mode: optional>` or `test <problem_folder_name> <language:cpp or py or java> <is_debug_mode: optional>`

- Run solution with input file.
`cptool run <input_file_path> <language:cpp or py or java>` or `run <input_file_path> <language:cpp or py or java>`
