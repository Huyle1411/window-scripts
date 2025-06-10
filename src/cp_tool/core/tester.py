import glob
import os
import subprocess
import sys
from pathlib import Path
from typing import Optional


class SolutionTester:
    def __init__(self, debug: bool = False):
        self.debug = debug

    @staticmethod
    def compare_files(file1: Path, file2: Path) -> bool:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            content1 = f1.readlines()
            content2 = f2.readlines()

        def normalize_content(file):
            return [line.rstrip() for line in file if line.strip()]

        normalized_content1 = normalize_content(content1)
        normalized_content2 = normalize_content(content2)

        return normalized_content1 == normalized_content2

    @staticmethod
    def print_file_content(file_path: Path) -> None:
        try:
            print(file_path.read_text())
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def print_io_file(self, input_file: Path, actual_file: Path, expected_file: Path) -> None:
        print("\033[93mInput:\033[0m")
        self.print_file_content(input_file)
        print("\033[93mOutput:\033[0m")
        self.print_file_content(actual_file)
        print("\033[93mExpected:\033[0m")
        self.print_file_content(expected_file)

    def compile_if_needed(self, file_path: Path, lang: str) -> Optional[str]:
        """Compiles the source file if needed and returns the execution command"""
        if lang == "cpp":
            try:
                command = f"build.cmd {file_path}.cpp"
                result = subprocess.run(command, shell=True)
                if result.returncode != 0:
                    return None
                return str(file_path) + ".exe"
            except subprocess.CalledProcessError as e:
                print(f"Error compiling cpp: {e}")
                return None
        elif lang == "java":
            try:
                command = f"build_java.cmd {file_path}.java"
                result = subprocess.run(command, shell=True)
                if result.returncode != 0:
                    return None
                return f"java -cp {file_path.parent} {file_path.name}"
            except subprocess.CalledProcessError as e:
                print(f"Error compiling java: {e}")
                return None
        elif lang == "kt":
            try:
                command = f"build_kotlin.cmd {file_path}.kt"
                result = subprocess.run(command, shell=True)
                if result.returncode != 0:
                    return None
                return f"java -jar {file_path}.jar"
            except subprocess.CalledProcessError as e:
                print(f"Error compiling kotlin: {e}")
                return None
        else:  # Python or other interpreted languages
            return str(file_path) + "." + lang

    def test_all_files(self, problem_dir: Path, lang: str, file_pattern: str = "sample-{index}") -> None:
        # Clean up previous results
        test_dir = problem_dir / "test"
        for res_file in test_dir.glob("*.res"):
            res_file.unlink()

        # Prepare execution command
        execute_cmd = self.compile_if_needed(problem_dir / "Main", lang)
        if not execute_cmd:
            return

        index, correct = 1, 0
        while True:
            input_file = test_dir / f"{file_pattern.format(index=index)}.in"
            expected_file = test_dir / f"{file_pattern.format(index=index)}.out"
            actual_file = test_dir / f"{file_pattern.format(index=index)}.res"

            if not expected_file.exists() and not actual_file.exists():
                break

            try:
                command = f"{execute_cmd} < {input_file} > {actual_file}"
                result = subprocess.run(command, shell=True)
                if result.returncode != 0:
                    return
            except subprocess.CalledProcessError as e:
                print(f"Error running: {e}")
                return

            if not expected_file.exists() or not actual_file.exists():
                print("Something wrong !!! File doesn't match between actual and expected output")
                return

            if self.compare_files(expected_file, actual_file):
                correct += 1
                print(f"Test case {index}: \033[92mAccepted\033[0m")
                if self.debug:
                    self.print_io_file(input_file, actual_file, expected_file)
            else:
                print(f"Test case {index}: \033[91mWrong Answer\033[0m")
                self.print_io_file(input_file, actual_file, expected_file)

            index += 1
        
        if index == 1:
            print("No test cases found")
        else:
            print(f"\033[92m{correct}/{index - 1}\033[0m test cases passed")


def main():
    if len(sys.argv) < 3:
        print("Please specify problem name and language to run")
        sys.exit(1)

    problem_dir = Path(sys.argv[1])
    lang = sys.argv[2]
    debug = bool(int(sys.argv[3])) if len(sys.argv) >= 4 else False

    tester = SolutionTester(debug=debug)
    tester.test_all_files(problem_dir, lang)


if __name__ == "__main__":
    main()
