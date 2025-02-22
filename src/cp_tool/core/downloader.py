import argparse
import json
import logging
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from typing import Optional
import re
import shutil
import sys
from cp_tool.config import PROJECT_ROOT
from datetime import datetime

sys.path.append(str(Path(__file__).parent.parent.parent))

from cp_tool.config import *
from cp_tool.version import VERSION

logger = logging.getLogger(__name__)


class CompetitiveProgrammingError(Exception):
    """Base exception for competitive programming tool errors"""

    pass


class ProblemCreationError(CompetitiveProgrammingError):
    """Raised when problem folder creation fails"""

    pass


class ColoredFormatter(logging.Formatter):
    COLORS = {"WARNING": YELLOW, "ERROR": RED}

    def format(self, record):
        level = record.levelname
        if level in self.COLORS:
            record.levelname = f"{self.COLORS[level]}{level}{RESET}"
        return super().format(record)


class CompetitiveCompanionHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, received_data=None, request_count=None, **kwargs):
        self.received_data = received_data if received_data is not None else []
        self.request_count = (
            request_count if request_count is not None else {"count": 0}
        )
        super().__init__(*args, **kwargs)

    def do_POST(self):
        self.request_count["count"] += 1
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        json_data = json.loads(post_data.decode("utf-8"))

        logger.info("Received json data")
        logger.info(json_data)
        self.received_data.append(json_data)

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response = json.dumps({"status": "success"})
        self.wfile.write(response.encode("utf-8"))


class TestCaseDownloader:
    def __init__(self):
        log_dir = PROJECT_ROOT / "logs"
        log_dir.mkdir(exist_ok=True)  # Create logs directory if it doesn't exist
        log_filename = f"log_{datetime.now().strftime('%Y-%m-%d')}.txt"
        self.init_logger(log_dir / log_filename)
        self.version = VERSION

    @staticmethod
    def init_logger(log_file: Optional[Path] = None) -> None:
        logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(log_file) if log_file else logging.StreamHandler()
        handler.setFormatter(ColoredFormatter(LOG_FORMAT))
        logger.addHandler(handler)

    def get_version(self) -> str:
        return str(self.version)

    def get_problem_name(self, data: dict) -> str:
        # USACO specific handling
        if "USACO" in data.get("group", ""):
            if "fileName" in data.get("input", {}):
                names = [
                    data["input"]["fileName"].rstrip(".in"),
                    data["output"]["fileName"].rstrip(".out"),
                ]
                if len(set(names)) == 1:
                    return names[0]

        # CodeChef specific handling
        if data.get("url", "").startswith("https://www.codechef.com"):
            return data["url"].rstrip("/").rsplit("/")[-1]

        # General case
        pattern_match = re.compile(NAME_PATTERN).search(data.get("name", ""))
        if pattern_match:
            return pattern_match.group(1)

        logger.info(
            "Could not automatically determine problem name: %s",
            json.dumps(data, indent=2),
        )
        return input("Enter name for this problem: ")

    def save_samples(self, json_data: dict, problem_path: Path) -> None:
        for i, test in enumerate(json_data["tests"], start=1):
            (problem_path / f"sample-{i}.in").write_text(test["input"])
            (problem_path / f"sample-{i}.out").write_text(test["output"])

    def create_problem_folder(
        self, json_data: Optional[dict] = None, problem_name: Optional[str] = None
    ) -> bool:
        try:
            if not json_data and not problem_name:
                raise ProblemCreationError("Both data and folder name are invalid")

            if not problem_name:
                problem_name = self.get_problem_name(json_data)

            logger.info("Creating problem folder: %s", problem_name)

            problem_path = Path(problem_name)
            problem_path.mkdir(exist_ok=True)

            test_path = problem_path / "test"
            test_path.mkdir(exist_ok=True)

            # Create solution files from templates
            for ext in SUPPORTED_LANGUAGE_EXTENSION:
                solution_file = problem_path / f"{problem_name}.{ext}"
                if not solution_file.exists():
                    try:
                        shutil.copy(TEMPLATE_PATH / f"template.{ext}", solution_file)
                    except FileNotFoundError:
                        logger.error(f"Template file not found: template.{ext}")

            if json_data:
                logger.info("Saving samples...")
                self.save_samples(json_data, test_path)

            print(f"{GREEN}{problem_name} is created{RESET}")
            return True

        except Exception as e:
            logger.error("Failed to create problem folder: %s", str(e))
            return False

    def listen_from_competitive_companion(self, max_requests: int):
        received_data = []
        request_count = {"count": 0}

        handler = lambda *args, **kwargs: CompetitiveCompanionHandler(
            *args, received_data=received_data, request_count=request_count, **kwargs
        )

        server_address = (HOST, PORT)
        httpd = HTTPServer(server_address, handler)

        try:
            while request_count["count"] < max_requests:
                httpd.handle_request()
        except KeyboardInterrupt:
            pass
        finally:
            httpd.server_close()
            logger.info("Server stopped!!!")

        if len(received_data) != max_requests:
            logger.warning(
                "Something wrong !!!. Data size: %d, total request: %d",
                len(received_data),
                max_requests,
            )

        return received_data

    def prepare_problems(self, names: list[str], need_to_download=False) -> bool:
        res = True
        datas = None

        if need_to_download:
            datas = self.listen_from_competitive_companion(len(names))

        for i in range(len(names)):
            if not self.create_problem_folder(
                json_data=(None if datas is None else datas[i]), problem_name=names[i]
            ):
                logger.warning("Cannot create folder %s", names[i])
                res = False

        return res

    def download_by_number(self, total_problems: int) -> bool:
        datas = self.listen_from_competitive_companion(total_problems)
        res = True
        for data in datas:
            if not self.create_problem_folder(json_data=data):
                logger.warning("Cannot create folder with this data")
                res = False

        return res


def main():
    parser = argparse.ArgumentParser(description="Tool for competitive programming")
    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version=f"%(prog)s {VERSION}",
    )
    parser.add_argument("--prepare", "-p", nargs="+", help="create problem folder")
    parser.add_argument(
        "--number", "-nu", type=int, help="download samples of problem by NUMBER"
    )
    parser.add_argument(
        "--name", "-na", nargs="+", help="download samples of problem by NAME"
    )

    args = parser.parse_args()
    downloader = TestCaseDownloader()

    if args.prepare:
        if not downloader.prepare_problems(args.prepare):
            return 1
    elif args.name:
        if not downloader.prepare_problems(args.name, True):
            return 1
    elif args.number:
        if not downloader.download_by_number(args.number):
            return 1
    else:
        parser.print_help()
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
