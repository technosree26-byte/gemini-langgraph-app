def input_router(state):

    if state["uploaded_file"] is not None:

        return "retriever"

    return "translator"


def speech_router(state):

    if state["generate_audio"]:

        return "speech"

    return "output"
