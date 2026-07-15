# Translation UI component
import streamlit as st


def text_input_box():
    """
    Display text input.
    """

    text = st.text_area(
        "Enter Text",
        height=250,
        placeholder="Type or paste text here...",
    )

    return text


def translate_button():
    return st.button(
        "Translate",
        use_container_width=True,
    )


def show_translation(translated_text: str):
    st.subheader("Translated Text")

    st.text_area(
        label="Output",
        value=translated_text,
        height=250,
        disabled=True,
    )