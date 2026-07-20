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
    """
    Return a normalized lower-case key for `name`
    if supported, otherwise return an empty string.
    """

    if not name:
        return ""

    key = name.strip().lower()

    # Accept both keys and display names
    for k, v in SUPPORTED_LANGUAGES.items():
        if key == k or key == v.lower():
            return k

    return ""


def is_supported_language(name: str) -> bool:
    """
    Return True if the language is supported.
    """

    return bool(normalize_language(name))


def validate_source_language(name: str) -> bool:
    """
    Source language may include Auto Detect.
    """

    return is_supported_language(name)


def validate_target_language(name: str) -> bool:
    """
    Target language cannot be Auto Detect.
    """

    normalized = normalize_language(name)

    return normalized not in ("auto", "")