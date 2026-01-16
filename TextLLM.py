import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(
    page_title="Text Summarizer",
    page_icon="📑",
    layout="centered"
)

st.markdown("""
<style>
.main {
    background-color: #f9fafb;
}

.title-text {
    font-size: 36px;
    font-weight: 700;
    text-align: center;
    color: #808080;
}

.subtitle-text {
    text-align: center;
    font-size: 16px;
    color: #6b7280;
    margin-bottom: 25px;
}

.card {
    background-color: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.08);
    margin-bottom: 20px;
}

.summary-box {
    background-color: #ecfeff;
    padding: 20px;
    border-radius: 10px;
    border-left: 6px solid #06b6d4;
    color: #0f172a;
    font-size: 15px;
}

.footer {
    text-align: center;
    color: #9ca3af;
    font-size: 13px;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

#API CONFIG
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

st.markdown('<div class="title-text">📑 Text Summarizer</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle-text">Paste any long text and get a clear, concise AI-generated summary</div>',
    unsafe_allow_html=True
)

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    input_text = st.text_area(
        "Enter text to summarize",
        height=250,
        placeholder="Paste your article, research paper, or notes here..."
    )

    word_count = len(input_text.split())
    st.caption(f"📝 Word count: {word_count}")

    summarize_btn = st.button("✨ Generate Summary")

    st.markdown('</div>', unsafe_allow_html=True)

if summarize_btn:
    if not input_text.strip():
        st.warning("Please enter some text before summarizing.")
    else:
        with st.spinner("Generating summary using Gemini..."):
            response = model.generate_content(
                f"Summarize the following text in a concise and clear manner:\n\n{input_text}"
            )

            summary = response.text.strip()

        st.subheader("📌 Summary")
        st.markdown(f'<div class="summary-box">{summary}</div>', unsafe_allow_html=True)

        st.download_button(
            label="📥 Download Summary",
            data=summary,
            file_name="summary.txt",
            mime="text/plain"
        )

st.markdown(
    '<div class="footer">Built with Streamlit & Google Gemini</div>',
    unsafe_allow_html=True
)
