"""
Audio Playback UI Component
"""

import os
from pathlib import Path

import streamlit as st


def display_audio(audio_path: str):
    """
    Display generated speech.
    """

    if not audio_path:
        return

    if not os.path.exists(audio_path):
        return

    st.markdown(
        """
### 🔊 Speech Output

Listen to the translated text or download the generated MP3.
"""
    )

    with open(audio_path, "rb") as audio_file:

        audio_bytes = audio_file.read()

    st.audio(
        audio_bytes,
        format="audio/mp3",
    )

    file_size = os.path.getsize(audio_path) / 1024

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Audio Format",
            "MP3",
        )

    with c2:
        st.metric(
            "File Size",
            f"{file_size:.1f} KB",
        )

    st.download_button(
        label="⬇ Download Speech",
        data=audio_bytes,
        file_name=Path(audio_path).name,
        mime="audio/mpeg",
        use_container_width=True,
    )