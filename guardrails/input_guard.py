"""Input validation helpers for guardrails.

Keep these checks lightweight and deterministic so they can be used
in synchronous UI paths and unit tests.
"""
from typing import Tuple


def is_valid_input(text: str) -> bool:
    """Return True if `text` is a non-empty string within limits."""
    if not isinstance(text, str):
        return False
    t = text.strip()
    if not t:
        return False
    # Arbitrary upper limit to avoid huge inputs
    if len(t) > 20000:
        return False
    return True


def validate_input_text(text: str) -> Tuple[bool, str]:
    """Validate input text returning (is_valid, reason)."""
    if not isinstance(text, str):
        return False, "Input must be a string"
    if not text.strip():
        return False, "Input is empty"
    if len(text) > 20000:
        return False, "Input is too long"
    return True, ""
