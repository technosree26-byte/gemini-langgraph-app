# Audio playback UI component
import streamlit as st
import os


def display_audio(audio_path: str):
    """
    Display generated audio if available.
    """

    if audio_path and os.path.exists(audio_path):

        st.subheader("Speech Output")

        audio_file = open(audio_path, "rb")

        st.audio(audio_file.read())

        with open(audio_path, "rb") as file:
            st.download_button(
                "Download MP3",
                file,
                file_name="translation.mp3",
                mime="audio/mp3",
            )