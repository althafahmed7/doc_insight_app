import streamlit as st
from pdf_utils import extract_text_from_pdf
from gpt4_utils import extract_fields_from_text
import json
import tempfile
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env

st.set_page_config(page_title="AI Document Insight")
st.title("📄 AI Document Insight Platform")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    st.success("✅ PDF Uploaded")

    with st.spinner("📖 Extracting text from PDF..."):
        raw_text = extract_text_from_pdf(tmp_path)

    st.subheader("📝 Extracted Text")
    st.text_area("Raw Text from PDF", raw_text, height=300)

    if st.button("🤖 Analyze with GPT-4"):
        with st.spinner("Sending to GPT-4..."):
            extracted_json = extract_fields_from_text(raw_text)
            try:
                structured = json.loads(extracted_json)
                st.success("✅ Structured Data from GPT-4")
                st.json(structured)
            except:
                st.error("❌ GPT-4 returned invalid JSON")
                st.text(extracted_json)
else:
    st.info("Please upload a PDF to begin.")
