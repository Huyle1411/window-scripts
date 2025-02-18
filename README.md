# How to use

**Set PATH in environment variables to run script globally**

- Compile/run C++ file. If `is_run == 1`, run after compile successful  
`build <filename.cpp> <is_run: optional>`

- Download sample test cases, make folder problem, ... For more information, run: `dl -h`  

- Test solution with sample test cases, support C++/Python. If `is_debug_mode != 0`, always print input, actual_output and expected_output. Otherwise, print `Accepted/Wrong Answer`.   
`test <problem_folder_name> <language:cpp or py> <is_debug_mode: optional>`
