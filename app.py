import streamlit as st
from chat.chat_state import ChatState
from chat.input_router import route_input
from file_processing.file_loader import handle_file

st.set_page_config(page_title="Legal Advisor Chat", page_icon="⚖️", layout="wide")
st.title("⚖️ Legal Advisor Chat")

if "chat_state" not in st.session_state:
    st.session_state.chat_state = ChatState()

uploaded_files = st.file_uploader("Upload legal documents(PDF / Image / TXT)", accept_multiple_files=True)
if uploaded_files:
    for file in uploaded_files:
        try:
            doc = handle_file(file)
            st.session_state.chat_state.add_document(doc)  # FIXED: was st.session.state
        except Exception as e:
            st.error(f"Error processing file {file.name}: {e}")

for turn in st.session_state.chat_state.get_history():
    st.markdown(f"**User:** {turn['user']}")
    st.markdown(f"**Assistant:** {turn['assistant']}")

query = st.text_input("Enter your legal question or request:")
if query:
    response = route_input(query, st.session_state.chat_state)
    st.markdown(f"**User:** {query}")
    st.markdown(f"**Assistant:** {response}")
