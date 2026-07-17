def input_router(state):

    if state["uploaded_file"] is not None:

        return "retriever"

    return "translator"


def speech_router(state):

    if state["generate_audio"]:

        return "speech"

    return "output"

builder.add_conditional_edges(
    "validator",
    input_router,
    {
        "retriever": "retriever",
        "translator": "translator",
    },
)

builder.add_conditional_edges(
    "translator",
    speech_router,
    {
        "speech": "speech",
        "output": END,
    },
)
