from pathlib import Path
import os

VERSION = "2.0"
HOST = "127.0.0.1"
PORT = 10043

# Colors
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
RESET = "\033[0m"

# File settings
NAME_PATTERN = r"^(?:Problem )?([A-Z][0-9]*)\b"
SUPPORTED_LANGUAGE_EXTENSION = ["cpp", "py", "java"]
PROJECT_ROOT = Path(os.getenv("CP_TOOL_ROOT"))
if PROJECT_ROOT is None:
    raise EnvironmentError(
        "CP_TOOL_ROOT environment variable is not set. Please run setup.cmd first."
    )
TEMPLATE_PATH = PROJECT_ROOT / "template"

# Logging
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(funcName)s(): %(lineno)d  %(message)s"
