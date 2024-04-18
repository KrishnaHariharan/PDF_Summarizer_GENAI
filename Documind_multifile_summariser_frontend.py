import streamlit as st
import os
from constants import openai_api_key
from Documind_multifile_summariser_backend import *

def main():
    #Set Page Configuration
    st.set_page_config(page_title="Documind")

    #Setting up the Page Layout
    st.title("TATA DOCUMIND")
    st.write("Summarize your confidential PDFs in seconds")
    st.divider()
    st.markdown("""
    <style>
        .stTextInput {
            position: fixed;
            bottom: 5%;
            width: 50%;
            padding: 10px;
            box-sizing: border-box;
        }
        </style>
        """, unsafe_allow_html=True)
    #st.text_input(label="",placeholder="Query your document")

    

    with st.sidebar:
        st.subheader("Your Documents")
        #Creating File Uploader Widget to Upload PDF
        pdf = st.file_uploader('Upload your PDF Document', type = 'pdf', accept_multiple_files=True)

        #Creating a Button for Users to Submit PDF for summarization
        submit = st.button("Upload")

    #Using the openai key
    os.environ["OPENAI_API_KEY"] = openai_api_key 

    if submit:
        st.subheader('Summary of the Files:')
        with st.spinner("Getting your PDF Ready for Query"):
            process_pdf_text(pdf)

if __name__ == "__main__":
    main()