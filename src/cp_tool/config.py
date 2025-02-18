from pathlib import Path

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
TEMPLATE_PATH = Path("D:/3.Personal/CompetitiveProgramming/template/")

# Logging
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(funcName)s(): %(lineno)d  %(message)s"
