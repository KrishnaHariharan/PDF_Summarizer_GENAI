import os
from constants import openai_api_key
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
import streamlit as st
from PyPDF2 import PdfReader
from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import ChatOpenAI



def multi_pdf_summariser(vectorstore):

    query = "Summarize the content of the uploaded PDF in 4-5 sentences. Start answer with File Name"

    if query:
        docs = vectorstore.similarity_search(query)
        
    chain = load_qa_chain(OpenAI(), chain_type = "stuff")
    summary = chain.run(input_documents=docs, question = query)
    st.write(summary)


def vector_store(text_chunks):
    #Embedding the Texts
    embeddings = OpenAIEmbeddings()

    #FAISS - Create Vector Store
    vectorstore = FAISS.from_texts(text_chunks, embeddings)

    multi_pdf_summariser(vectorstore)


def get_text_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator = "\n",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )
    text_chunks = text_splitter.split_text(text = raw_text)
    vector_store(text_chunks)

def process_pdf_text(pdf):
    if pdf is not None:
        raw_text = ""
        count = 0
        for files in pdf:
            pdf_reader =PdfReader(files)
            for page in pdf_reader.pages:
                raw_text += page.extract_text() 
            get_text_chunks(raw_text)
        
            


