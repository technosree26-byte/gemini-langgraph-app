from services.file_service import extract_text


def retriever_node(state):
    try:
        uploaded_file = state["uploaded_file"]
        state["input_text"] = extract_text(uploaded_file)
    except Exception as e:
        state["error"] = f"File extraction failed: {e}"
    return state
