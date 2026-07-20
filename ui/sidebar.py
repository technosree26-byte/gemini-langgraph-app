"""
Sidebar UI component
"""

import streamlit as st


def render_sidebar():
    """
    Render application sidebar.
    Returns
    -------
    source_language
    target_language
    """

    st.sidebar.markdown(
        """
        <h2 style='text-align:center;color:#2496ED;'>
            🌍 AI Translator
        </h2>
        """,
        unsafe_allow_html=True,
    )

    #st.sidebar.markdown("---")

    st.sidebar.subheader("🌐 Translation Settings")

    source_language = st.sidebar.selectbox(
        "Source Language",
        (
            "Auto Detect",
            "English",
            "French",
            "Spanish",
            "German",
            "Hindi",
            "Tamil",
            "Chinese",
            "Japanese",
        ),
    )

    target_language = st.sidebar.selectbox(
        "Target Language",
        (
            "English",
            "French",
            "Spanish",
            "German",
            "Hindi",
            "Tamil",
            "Chinese",
            "Japanese",
        ),
    )

    #st.sidebar.markdown("---")

    #st.sidebar.subheader("📄 Supported Files")

    #st.sidebar.success("✓ PDF")
    #st.sidebar.success("✓ TXT")
    #st.sidebar.success("✓ CSV")
    #st.sidebar.success("✓ Excel (.xlsx, .xls)")

    st.sidebar.markdown("---")

    st.sidebar.subheader("🎙 Features")

    st.sidebar.write("✅ AI Translation")
    st.sidebar.write("✅ LangGraph Workflow")
    st.sidebar.write("✅ Speech Generation")
    st.sidebar.write("✅ Document Translation")

    st.sidebar.markdown("---")

    st.sidebar.info(
        """
**Powered By**

- Google Gemini-3.5-flash
- LangGraph
- Streamlit
- gTTS Speech
"""
    )

    st.sidebar.markdown(
        """
<div style="text-align:center;
            color:gray;
            font-size:12px;
            padding-top:20px;">
Version 1.0.0
</div>
""",
        unsafe_allow_html=True,
    )

    return source_language, target_language