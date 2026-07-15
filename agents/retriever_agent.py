from services.file_service import extract_text


def retriever_node(state):

    uploaded_file = state["uploaded_file"]

    extracted_text = extract_text(uploaded_file)

    state["input_text"] = extracted_text

    return state
