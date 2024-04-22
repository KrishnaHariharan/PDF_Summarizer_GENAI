import streamlit as st
import os
from constants import openai_api_key
from PDF_summariser_backend import *

def main():

    #Set Page Configuration
    st.set_page_config(page_title="Summarizer", layout = "wide")

    #Setting up the Page Layout
    st.title("PDF SUMMARIZER")
    st.write("Summarize your Confidential PDFs in seconds")
    st.divider()
    # Add custom CSS to change the background color of the sidebar
    st.markdown("""
        <style>
            .st-emotion-cache-vk3wp9.eczjsme11{ 
                background-color: #EAEAEA;  /* Sidebar Background */
                color: #333333;
            }
        </style>
    """, unsafe_allow_html=True)
    #Buttons
    st.markdown("""
        <style>
            .st-emotion-cache-13ejsyy.ef3psqc12{ 
                background-color: #008080;  /* Sidebar Background */
                color: #EAEAEA
            }
        </style>
    """, unsafe_allow_html=True)
    #Upload Box
    st.markdown("""
        <style>
            .st-emotion-cache-taue2i.e1b2p2ww15{ 
                background-color: #F5F5F5;  /* Sidebar Background */
                border: 1px solid #008080;
                
            }
        </style>
    """, unsafe_allow_html=True)

    #Both Main Title
    st.markdown("""
        <style>
            .st-emotion-cache-10trblm.e1nzilvr1{ 
                color: #008080;
            }
        </style>
    """, unsafe_allow_html=True)

    





    with st.sidebar:
        st.subheader("Summarizer")
        st.sidebar.image("C:/Users/91828/Documents/GitHub/PDF_Summarizer_GENAI/pdf.png", use_column_width=True)
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