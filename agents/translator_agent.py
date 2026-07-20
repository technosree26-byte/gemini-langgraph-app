"""
Translator Agent
"""

from services.gemini_service import GeminiTranslator
from guardrails.prompt_guard import sanitize_prompt


def translator_node(state, translator=None):
    """
    Translate text using Gemini.

    During normal execution, a GeminiTranslator is created.
    During testing, a fake translator can be injected.
    """

    # --------------------------------------------
    # Prompt Guard
    # --------------------------------------------

    clean_text, truncated = sanitize_prompt(
        state["input_text"]
    )

    state["input_text"] = clean_text

    if truncated:
        state["warning"] = (
            "Input exceeded the maximum length and was truncated."
        )
    else:
        state["warning"] = ""

    # --------------------------------------------
    # Translator
    # --------------------------------------------

    if translator is None:
        translator = GeminiTranslator()

    try:

        translated_text = translator.translate(
            text=state["input_text"],
            source_language=state["source_language"],
            target_language=state["target_language"],
        )

        state["translated_text"] = translated_text
        state["error"] = ""

    except Exception as e:

        state["translated_text"] = ""
        state["error"] = str(e)

    return state