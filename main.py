import streamlit as st
import tempfile, os  
from dotenv import load_dotenv 
from Loading_Chunking import load_and_chunk_pdf      
from Vector_Databases import build_vectorstore
from api_groq import ask_groq

load_dotenv()

# webpage configuration
st.set_page_config(page_title="RAG with Groq", page_icon="📚")
st.title("RAG with Groq: PDF Q&A")
st.caption("Upload a PDF, and ask questions about its content!")
# file uploader

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

    # Load and chunk the PDF + store in ChromaDB
    if "collection" not in st.session_state:
        with st.spinner("Processing PDF"):
            chunks = load_and_chunk_pdf(tmp_file_path)
            st.session_state.collection = build_vectorstore(chunks)
        st.success("PDF processed and stored in vector database!")
    # chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    # show pervious Q&A
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    # user input
    question = st.chat_input("Ask a question about your PDF...")

    if question:
        # Show user message
        with st.chat_message("user"):
            st.write(question)
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )

        # Get + show answer
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = ask_groq(question, st.session_state.collection)
            st.write(answer)
        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )





    