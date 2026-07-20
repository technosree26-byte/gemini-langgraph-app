import streamlit as st


def hero():
    """
    Render the hero banner.
    """

    st.markdown(
        """
<div class="hero">
    <h1>🌍 AI Translation Agent</h1>
    <p>
        End-to-end multilingual translation powered by
        <strong>Google Gemini</strong>, <strong>LangGraph</strong>,
        and <strong>Streamlit</strong>.
    </p>
    <p>
        Translate text, PDFs, CSV files, and Excel documents,
        then generate downloadable MP3 speech from the translated output.
    </p>
</div>
""",
        unsafe_allow_html=True,
    )


def start_card():
    st.markdown(
        """
<div style="background:#F5F7FF;padding:20px;border-radius:12px;box-shadow:0 4px 20px rgba(0,0,0,0.05);">
    <h3 style="margin:0; color:#0A3D62;">Start Translation</h3>
    <p style="margin:5px 0 0; color:#34495E;">
        Enter text or upload a document, then choose source and target languages.
    </p>
</div>
""",
        unsafe_allow_html=True,
    )


def end_card():
    st.markdown(
        """
<div style="background:#E9F7EF;padding:20px;border-radius:12px;box-shadow:0 4px 20px rgba(0,0,0,0.05);">
    <h3 style="margin:0; color:#117A65;">Ready to translate</h3>
    <p style="margin:5px 0 0; color:#2E4053;">
        Press Translate once you've entered text and selected languages.
    </p>
</div>
""",
        unsafe_allow_html=True,
    )


def status_bar():
    st.markdown(
        """
<div style="display:flex;gap:10px;flex-wrap:wrap;">

<span style="
background:#E8F5E9;
padding:8px 16px;
border-radius:30px;
font-weight:600;">
    ✅ Gemini
</span>

<span style="
background:#E3F2FD;
padding:8px 16px;
border-radius:30px;
font-weight:600;">
    🧠 LangGraph
</span>

<span style="
background:#FFF3E0;
padding:8px 16px;
border-radius:30px;
font-weight:600;">
    🔊 Speech
</span>

</div>
""",
        unsafe_allow_html=True,
    )