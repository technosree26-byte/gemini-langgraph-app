# Sidebar UI component
import streamlit as st


def render_sidebar():
    """
    Render the application sidebar.
    Returns:
        source_lang, target_lang
    """

    st.sidebar.title("⚙️ Settings")

    source_language = st.sidebar.selectbox(
        "Source Language",
        [
            "Auto Detect",
            "English",
            "French",
            "Spanish",
            "German",
            "Hindi",
            "Tamil",
            "Chinese",
            "Japanese",
        ],
    )

    target_language = st.sidebar.selectbox(
        "Target Language",
        [
            "English",
            "French",
            "Spanish",
            "German",
            "Hindi",
            "Tamil",
            "Chinese",
            "Japanese",
        ],
    )

    st.sidebar.markdown("---")
    st.sidebar.info(
        "LangGraph Translation Agent\n\n"
        "Supports text translation, document translation, and speech synthesis."
    )

    return source_language, target_language