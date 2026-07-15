def validator_node(state):

    if state["uploaded_file"] is None:

        if not state["input_text"].strip():

            state["error"] = "Please enter text."

    return state