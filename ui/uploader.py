# File uploader UI component
import streamlit as st


SUPPORTED_TYPES = [
    "txt",
    "pdf",
    "csv",
    "xlsx",
]


def upload_document():
    """
    Returns uploaded file.
    """

    uploaded_file = st.file_uploader(
        "Upload a document",
        type=SUPPORTED_TYPES,
    )

    return uploaded_file