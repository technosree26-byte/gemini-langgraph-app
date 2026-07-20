def validator_node(state):
    """
    Validate that either text or a file is provided.
    """

    state["error"] = ""

    if state["uploaded_file"] is None:

        if not state["input_text"].strip():

            state["error"] = "Please enter text."

    return state