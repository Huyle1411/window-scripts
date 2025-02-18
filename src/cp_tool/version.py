from dataclasses import dataclass
from typing import Tuple


@dataclass
class Version:
    major: int
    minor: int
    patch: int

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"

    def to_tuple(self) -> Tuple[int, int, int]:
        return (self.major, self.minor, self.patch)


# Current version
CURRENT_VERSION = Version(2, 1, 0)
VERSION = str(CURRENT_VERSION)
