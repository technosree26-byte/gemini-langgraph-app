"""
Translation UI Component
"""

import streamlit as st


def text_input_box():
    """
    Input text area.
    """

    st.markdown(
        """
### 📝 Enter Text

Type or paste the text you want to translate.
"""
    )

    return st.text_area(
        label="",
        height=260,
        placeholder="Start typing here...",
        label_visibility="collapsed",
    )


def translate_button():

    st.markdown("<br>", unsafe_allow_html=True)

    return st.button(
        "🌍 Translate",
        use_container_width=True,
        type="primary",
    )


def show_translation(translated_text: str):

    st.markdown(
        """
### 🌐 Translation
"""
    )

    st.text_area(
        label="",
        value=translated_text,
        height=260,
        disabled=True,
        label_visibility="collapsed",
    )


def translation_statistics(source_text, translated_text):

    st.markdown("### 📊 Translation Statistics")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Characters",
            len(source_text),
        )

    with c2:
        st.metric(
            "Words",
            len(source_text.split()),
        )

    with c3:
        st.metric(
            "Translated",
            len(translated_text.split()),
        )

    with c4:
        st.metric(
            "Status",
            "✅ Done" if translated_text else "Waiting",
        )