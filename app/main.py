import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import streamlit as st

from app.graph import translation_graph

from guardrails.input_guard import validate_input_text
from guardrails.file_guard import is_allowed_file
from guardrails.language_guard import (
    validate_source_language,
    validate_target_language,
)

from ui.styles import load_css
from ui.cards import (
    hero,
    start_card,
    end_card,
    status_bar,
)

from ui.sidebar import render_sidebar
from ui.translator_ui import (
    text_input_box,
    translate_button,
    show_translation,
    translation_statistics,
)

from ui.uploader import upload_document
from ui.audio_player import display_audio

from services.file_service import extract_text

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Translation Agent",
    page_icon="🌍",
    layout="wide",
)

load_css()

hero()
status_bar()

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

source_language, target_language = render_sidebar()

# ---------------------------------------------------
# Session State
# ---------------------------------------------------

if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""

if "audio_path" not in st.session_state:
    st.session_state.audio_path = ""

# ---------------------------------------------------
# Layout
# ---------------------------------------------------

left, right = st.columns([1, 1], gap="large")

with left:

    start_card()

    #st.subheader("📝 Input")

    user_text = text_input_box()

    uploaded_file = upload_document()

    # File extraction
    if uploaded_file:

        if not is_allowed_file(uploaded_file.name):
            st.error("Unsupported file type.")
            st.stop()

        try:
            user_text = extract_text(uploaded_file)

        except Exception as e:
            st.error(f"Could not read uploaded file.\n\n{e}")
            st.stop()

    # Translate button belongs on the INPUT side
    translate = translate_button()

    end_card()
# ---------------------------------------------------

# Translation
# ---------------------------------------------------

if translate:

    # -----------------------------------------------
    # Language Guard
    # -----------------------------------------------

    if not validate_source_language(source_language):
        st.error("Unsupported source language.")
        st.stop()

    if not validate_target_language(target_language):
        st.error("Unsupported target language.")
        st.stop()

    # -----------------------------------------------
    # Input Guard
    # -----------------------------------------------

    is_valid, message = validate_input_text(user_text)

    if not is_valid:
        st.warning(message)
        st.stop()

    state = {

        "input_text": user_text,
        "uploaded_file": uploaded_file,
        "source_language": source_language,
        "target_language": target_language,
        "translated_text": "",
        "generate_audio": True,
        "audio_file": "",
        "error": "",
        "warning": "",

    }

    with st.spinner("🌍 Translating..."):

        result = translation_graph.invoke(state)
    #    st.write("DEBUG RESULT:", result)
    # -----------------------------------------------
    # Graph Error Handling
    # -----------------------------------------------

    if result.get("error"):

        st.error(result["error"])

    else:

        translated = result["translated_text"]

        st.session_state.translated_text = translated

        # Audio was already generated inside the LangGraph workflow
        st.session_state.audio_path = result.get("audio_file", "")

        # Optional warning from prompt guard
        if result.get("warning"):
            st.warning(result["warning"])

        st.toast("Translation completed ✅")

# ---------------------------------------------------
# Output
# ---------------------------------------------------

with right:

    st.subheader("🌐 Translation")

    if st.session_state.translated_text:

        show_translation(st.session_state.translated_text)

        translation_statistics(
            user_text,
            st.session_state.translated_text,
        )

        display_audio(st.session_state.audio_path)

    else:

        st.info("Translation will appear here after you click Translate.")