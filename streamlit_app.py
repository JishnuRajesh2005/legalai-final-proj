import streamlit as st
from llm_ollama.ollama_client import OllamaClient
from llm_ollama.prompt_builder import PromptBuilder

st.set_page_config(page_title="Legal AI Summarizer", layout="wide")

st.title("📄 Legal Document Summarizer AI")

user_input = st.text_area(
    "Paste your legal document here",
    height=300
)

if st.button("Summarize"):
    if user_input.strip():
        with st.spinner("Summarizing..."):
            llm = OllamaClient(model="llama3")
            prompt = PromptBuilder.build_summary_prompt(user_input)
            summary = llm.generate(prompt)

        st.subheader("Summary")
        st.write(summary)
    else:
        st.warning("Please enter some text")
