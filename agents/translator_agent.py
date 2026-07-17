"""
Translator Agent
"""

from services.gemini_service import GeminiTranslator


def translator_node(state, translator=None):
    """
    Translate text using Gemini.

    During normal execution, a GeminiTranslator is created.
    During testing, a fake translator can be injected.
    """

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