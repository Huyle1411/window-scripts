from dataclasses import dataclass
from typing import Tuple


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


# Current version
CURRENT_VERSION = Version.from_string("2.2.3")
VERSION = str(CURRENT_VERSION)
