import streamlit as st
import os
from constants import openai_api_key
from Documind_multifile_summariser_backend import *

def main():
    #Set Page Configuration
    st.set_page_config(page_title="Summariser")

    #Setting up the Page Layout
    st.title("DOCU SUMMARIZER")
    st.write("Summarize your confidential PDFs in seconds")
    st.divider()
    
    

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
        with st.spinner("Getting your PDF Summary Ready"):
            process_pdf_text(pdf)

if __name__ == "__main__":
    main()