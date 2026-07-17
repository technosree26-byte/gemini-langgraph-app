"""Language validation and normalization helpers."""

SUPPORTED_LANGUAGES = {
    "auto": "Auto Detect",
    "english": "English",
    "french": "French",
    "spanish": "Spanish",
    "german": "German",
    "hindi": "Hindi",
    "tamil": "Tamil",
    "chinese": "Chinese",
    "japanese": "Japanese",
}


def normalize_language(name: str) -> str:
    """Return a normalized lower-case key for `name` if supported, else empty string."""
    if not name:
        return ""
    key = name.strip().lower()
    # Accept display names as well as keys
    for k, v in SUPPORTED_LANGUAGES.items():
        if key == k or key == v.lower():
            return k
    return ""


def is_supported_language(name: str) -> bool:
    return bool(normalize_language(name))
