import sys, os, subprocess


def print_file_content(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def print_output(output):
    print("\033[93mOutput:\033[0m")
    print_file_content(output)


def run_program(subfolder, lang):
    file_name = subfolder + "\\" + subfolder
    execute_file = file_name + "." + lang

    # Compile if needed
    if lang == "cpp":
        try:
            command = f"build.cmd {file_name}.cpp"
            result = subprocess.run(command, shell=True)
            if result.returncode != 0:
                return
        except subprocess.CalledProcessError as e:
            print(f"Error running: {e}")
            return

        execute_file = file_name + ".exe"
    elif lang == "java":
        try:
            command = f"build_java.cmd {file_name}.java"
            result = subprocess.run(command, shell=True)
            if result.returncode != 0:
                return
        except subprocess.CalledProcessError as e:
            print(f"Error running: {e}")
            return

        execute_file = "java -cp " + subfolder + " " + subfolder

    output_file = os.path.join("temp_output.res")

    try:
        command = f"{execute_file} > {output_file}"
        result = subprocess.run(command, shell=True)
        if result.returncode != 0:
            print(f"Error running: {result.returncode}")
            return
    except subprocess.CalledProcessError as e:
        print(f"Error running: {e}")
        return

    print_output(output_file)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please specify problem name and language to run")
        sys.exit(1)

    subfolder = sys.argv[1]
    lang = sys.argv[2]
    run_program(subfolder, lang)
