"""
Routing functions for LangGraph.
"""


def input_router(state):
    """
    Route to the retriever if a file was uploaded,
    otherwise go directly to the translator.
    """

    if state["uploaded_file"] is not None:
        return "retriever"

    return "translator"


def speech_router(state):
    """
    Route to the speech node only when audio generation
    has been requested.
    """

    if state["generate_audio"]:
        return "speech"

    return "output"