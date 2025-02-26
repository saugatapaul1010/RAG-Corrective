import os
import sys

# Append the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import required modules
from operator import itemgetter
from langchain.docstore.document import Document
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
    NLTKTextSplitter,
    TokenTextSplitter,
    MarkdownTextSplitter,
)
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# Import API keys
from app_config.open_ai_cred import OPENAI_KEY, TAVILY_API_KEY, WEATHER_API_KEY

# Set environment variables
os.environ['OPENAI_API_KEY'] = OPENAI_KEY
os.environ['TAVILY_API_KEY'] = TAVILY_API_KEY

# Define data folder
data_folder = 'project_data'

class VectorStore:
    def __init__(self, model_name: str, embed_model_name: str):
        """
        Initializes the VectorStore class.

        Args:
            model_name (str): Name of the model.
            embed_model_name (str): Name of the embedding model.
        """
        self.model_name = model_name
        self.embed_model_name = embed_model_name

    def document_splitter(self, pdf_path: str):
        """
        Splits a PDF document into chunks.

        Args:
            pdf_path (str): Path to the PDF file.

        Returns:
            list: List of chunked documents.
        """
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunked_docs = text_splitter.split_documents(documents)
        print("...Splitting Done")  
        return chunked_docs

    def document_indexer(self, chunked_docs: list):    
        """
        Indexes the chunked documents using Chroma and OpenAI embeddings.

        Args:
            chunked_docs (list): List of chunked documents.
        """
        openai_embed_model = OpenAIEmbeddings(model=self.embed_model_name)
        Chroma.from_documents(
            documents=chunked_docs,
            collection_name='capstone_proj',
            embedding=openai_embed_model,
            collection_metadata={"hnsw:space": "cosine"},
            persist_directory="./proj_db"
        )
        print(".....Indexing done.....")

    def vectord_db_loader(self):
        """
        Loads the vector database from persistent storage.

        Returns:
            Chroma: Loaded Chroma vector database.
        """
        openai_embed_model = OpenAIEmbeddings(model=self.embed_model_name)
        chroma_db = Chroma(
            persist_directory="./proj_db",
            collection_name='capstone_proj',
            embedding_function=openai_embed_model
        )
        print(".....Loading vector DB....")
        return chroma_db
         


# vector_store = VectorStore(model_name , embed_model)
# chroma_db = vector_store.vectord_db_loader()
# count = chroma_db._collection.get(limit=5)
# print(count)

# pdf_file = os.listdir(data_folder)
# chunked_all_data = []
# for val in pdf_file :
#     pdf_path  = os.path.join(data_folder,val)
#     res = vector_store.document_splitter(pdf_path)
#     chunked_all_data.extend(res)
# print(len(chunked_all_data))
# vector_store.document_indexer(chunked_all_data)    
#print(pdf_file)