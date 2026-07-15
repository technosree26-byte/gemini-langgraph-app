from services.gtts_service import generate_audio


def speech_node(state):

    filename = generate_audio(
        state["translated_text"],
        state["target_language"],
    )

    state["audio_file"] = filename

    return state
