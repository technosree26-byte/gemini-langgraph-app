import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import streamlit as st

from app.graph import translation_graph

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
from agents.speech_agent import speech_node


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

    st.subheader("📝 Input")

    user_text = text_input_box()

    uploaded_file = upload_document()

    # Extract text from uploaded document
    if uploaded_file:
        user_text = extract_text(uploaded_file)

    # Input statistics
    if user_text.strip():

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Characters",
            len(user_text)
        )

        c2.metric(
            "Words",
            len(user_text.split())
        )

        c3.metric(
            "Target",
            target_language
        )

    end_card()

# ---------------------------------------------------
# Translation
# ---------------------------------------------------

translate = translate_button()

if translate:

    if user_text.strip():

        state = {
            "input_text": user_text,
            "uploaded_file": uploaded_file,
            "source_language": source_language,
            "target_language": target_language,
            "translated_text": "",
            "generate_audio": True,
            "audio_file": "",
            "error": "",
        }

        with st.spinner("🌍 Translating..."):

            result = translation_graph.invoke(state)

        if result.get("error"):

            st.error(result["error"])

        else:

            translated = result["translated_text"]

            st.session_state.translated_text = translated

            try:
                st.session_state.audio_path = speech_node(translated)

            except Exception:
                st.session_state.audio_path = ""

            st.toast("Translation completed ✅")

    else:

        st.warning("Please enter text or upload a document.")

# ---------------------------------------------------
# Output
# ---------------------------------------------------

with right:

    start_card()

    st.subheader("🌐 Translation")

    if st.session_state.translated_text:

        show_translation(
            st.session_state.translated_text
        )

        translation_statistics(
            user_text,
            st.session_state.translated_text,
        )

        display_audio(
            st.session_state.audio_path
        )

    else:

        st.info("Translation will appear here.")

    end_card()