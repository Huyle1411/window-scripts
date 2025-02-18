from dataclasses import dataclass
from typing import Tuple
import subprocess
from pathlib import Path

@dataclass
class Version:
    major: int
    minor: int
    patch: int
    
    @classmethod
    def from_string(cls, version_str: str) -> "Version":
        major, minor, patch = map(int, version_str.split("."))
        return cls(major=major, minor=minor, patch=patch)
    
    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"
    
    def to_tuple(self) -> Tuple[int, int, int]:
        return (self.major, self.minor, self.patch)
    
    def __lt__(self, other: "Version") -> bool:
        return self.to_tuple() < other.to_tuple()

# Current version
CURRENT_VERSION = Version(2, 0, 0)

def get_version() -> str:
    """Get version from git tags, fallback to default version if not available."""
    try:
        # Get the git root directory
        repo_root = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"], 
            universal_newlines=True
        ).strip()
        
        # Get the latest tag
        version = subprocess.check_output(
            ["git", "describe", "--tags"], 
            universal_newlines=True,
            cwd=repo_root
        ).strip()
        
        return version
    except subprocess.CalledProcessError:
        return "2.0.0"  # Fallback version

VERSION = get_version() 