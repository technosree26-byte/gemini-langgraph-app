"""Prompt sanitization helpers."""

import re
from typing import Tuple


_WHITESPACE_RE = re.compile(r"\s+")


def sanitize_prompt(prompt: str, max_length: int = 5000) -> Tuple[str, bool]:
    """Return a sanitized prompt and a boolean indicating whether it was truncated.

    Basic sanitization removes excessive whitespace and trims to `max_length`.
    """
    if not isinstance(prompt, str):
        return "", False
    p = _WHITESPACE_RE.sub(" ", prompt).strip()
    truncated = False
    if len(p) > max_length:
        p = p[:max_length]
        truncated = True
    return p, truncated
