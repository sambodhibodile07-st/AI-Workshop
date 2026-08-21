from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from pypdf import PdfReader
from torch import chunk

#Resume analyzer using RAG and LLM
# RAG Document Loader (retrieve the pdf file and extract the text from it)
def extract_pdf(file):
    reader = PdfReader(file)
    text = ""     #string to store the extracted text
    for page in reader.pages:
        text += page.extract_text()
    return text


#splitting text
def split_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    return splitter.split_text(text)

#Embedding and vector storage
def create_vector_store(text):
    chunks =split_text(text)
    docs=[Document(page_content=s) for s in chunks]
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(docs, embeddings)
    return vector_store