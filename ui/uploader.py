"""
Document Upload UI Component
"""

import streamlit as st

SUPPORTED_TYPES = [
    "txt",
    "pdf",
    "csv",
    "xlsx",
    "xls",
]


def upload_document():
    """
    Display a professional document uploader.
    Returns
    -------
    UploadedFile | None
    """

    st.markdown(
        """
### 📄 Upload Document

Upload a document to translate.

**Supported formats**

📕 PDF 📄 TXT 📊 CSV 📈 Excel (.xlsx, .xls)
"""
    )

    uploaded_file = st.file_uploader(
        label="Choose a document",
        type=SUPPORTED_TYPES,
        label_visibility="collapsed",
    )

    if uploaded_file is not None:

        size_mb = uploaded_file.size / (1024 * 1024)

        st.success(f"✅ **{uploaded_file.name}**")

        c1, c2 = st.columns(2)

        with c1:
            st.metric("Type", uploaded_file.name.split(".")[-1].upper())

        with c2:
            st.metric("Size", f"{size_mb:.2f} MB")

    return uploaded_file