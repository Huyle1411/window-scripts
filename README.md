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

- Download sample test cases, make folder problem, ... For more information, run:  
`cptool dl -h`  

- Test solution with sample test cases, support C++/Python/Java. If `is_debug_mode != 0`, always print input, actual_output and expected_output. Otherwise, print `Accepted/Wrong Answer`.   
`cptool test <problem_folder_name> <language:cpp or py or java> <is_debug_mode: optional>`
