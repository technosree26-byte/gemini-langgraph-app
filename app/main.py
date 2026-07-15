import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

# Main application entry point
import streamlit as st

from app.graph import translation_graph
from ui.sidebar import render_sidebar
from ui.uploader import upload_document
from ui.translator_ui import (
    text_input_box,
    translate_button,
    show_translation,
)
from ui.audio_player import display_audio


st.set_page_config(
    page_title="LangGraph Translator",
    page_icon="🌍",
    layout="wide",
)

st.title("🌍 AI Language Translation Agent")

st.write(
    """
Translate text or documents into multiple languages.
This UI will later connect to LangGraph agents.
"""
)

# -----------------------------
# Sidebar
# -----------------------------

source_language, target_language = render_sidebar()

# -----------------------------
# Input Section
# -----------------------------

left, right = st.columns(2)

with left:

    st.header("Input")

    user_text = text_input_box()

    uploaded_file = upload_document()

with right:

    st.header("Output")

    show_translation("Translation will appear here...")

# -----------------------------
# Translate Button
# -----------------------------

if translate_button():

    if uploaded_file is not None:

        st.success(f"Uploaded: {uploaded_file.name}")

    if user_text.strip():

        st.success("Text received successfully.")

        st.write("Source:", source_language)
        st.write("Target:", target_language)

        input_text = user_text
        source_lang = source_language
        target_lang = target_language

        state = {
            "input_text": input_text,
            "source_language": source_lang,
            "target_language": target_lang,
            "translated_text": "",
        }

        result = translation_graph.invoke(state)
        st.write(result["translated_text"])

    elif uploaded_file is None:

        st.warning("Please enter text or upload a document.")

# -----------------------------
# Audio Placeholder
# -----------------------------

display_audio("")