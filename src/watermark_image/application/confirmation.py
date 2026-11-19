"""@file confirmation.py
@brief The Confirmation DTO: the answer to a save.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Confirmation:
    """@brief Tells which file a picture was stored in."""

    target: Path
