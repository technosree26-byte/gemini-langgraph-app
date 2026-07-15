"""Shared graph state definitions."""
from typing import TypedDict


class TranslationState(TypedDict):

    input_text: str

    uploaded_file: object | None

    source_language: str

    target_language: str

    translated_text: str

    generate_audio: bool

    audio_file: str

    error: str