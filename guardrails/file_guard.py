"""File-related guard utilities."""
from pathlib import Path
from typing import Iterable


ALLOWED_EXTENSIONS = {"txt", "pdf", "csv", "xlsx"}


def is_allowed_file(filename: str, allowed: Iterable[str] = None) -> bool:
    """Return True if `filename` has an allowed extension.

    `allowed` can override the default `ALLOWED_EXTENSIONS` set.
    """
    if not filename:
        return False
    allowed_set = set(allowed) if allowed is not None else ALLOWED_EXTENSIONS
    return Path(filename).suffix.lower().lstrip(".") in allowed_set
