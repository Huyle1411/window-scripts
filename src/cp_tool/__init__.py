"""
Competitive Programming Tool - A tool to help with competitive programming tasks
"""

from cp_tool.version import VERSION as __version__
from cp_tool.core.downloader import TestCaseDownloader
from cp_tool.core.runner import run_program
from cp_tool.core.tester import SolutionTester

__all__ = [
    "TestCaseDownloader",
    "run_program",
    "SolutionTester",
]
