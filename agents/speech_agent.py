"""
Speech Agent
"""

from services.gtts_service import generate_audio


def speech_node(state):
    """
    Generate speech only if translated text exists.
    """

    translated_text = state.get("translated_text", "").strip()

    if not translated_text:
        state["audio_file"] = ""
        return state

    try:
        filename = generate_audio(
            translated_text,
            state["target_language"],
        )

        state["audio_file"] = filename

    except Exception as e:
        state["audio_file"] = ""
        state["error"] = f"Speech generation failed: {e}"

    return state