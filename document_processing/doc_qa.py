import os
import sys
from operator import itemgetter

# Add parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# LangChain and AI-related imports
from langchain_chroma import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
from langchain.text_splitter import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
    NLTKTextSplitter,
    TokenTextSplitter,
    MarkdownTextSplitter
)
from langchain_openai import ChatOpenAI
from langchain.document_loaders import PyPDFLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage

# Project-specific imports
from app_config.open_ai_cred import (
    OPENAI_KEY, TAVILY_API_KEY, WEATHER_API_KEY, MODEL_NAME, EMBED_MODEL
)
from document_processing.doc_indexer import VectorStore
from document_processing.proj_chains import (
    context_qa_chain, query_re_writer_agent, document_grader_agent
)
from document_processing.proj_lang_graph import agentic_rag_flow, retriever_call

# Set environment variables
os.environ['OPENAI_API_KEY'] = OPENAI_KEY
os.environ['TAVILY_API_KEY'] = TAVILY_API_KEY


def historical_qa_context(question: str):
    """
    Retrieves context-aware answers using a retrieval-augmented generation (RAG) approach.
    :param question: User's query
    """
    chatgpt = ChatOpenAI(model_name=MODEL_NAME, temperature=0)
    final_retriever = retriever_call()
    rag_chain = context_qa_chain(chatgpt, final_retriever)
    result = rag_chain.invoke({"input": question, "chat_history": []})
    print(result)


def agentic_qa(question: str, chat_history: list):
    """
    Uses an agentic RAG approach to answer queries while maintaining chat history.
    :param question: User's query
    :param chat_history: List of previous interactions
    :return: Generated response and updated chat history
    """
    agentic_rag = agentic_rag_flow()
    print(len(chat_history), "length of chat history")
    response = agentic_rag.invoke({"question": question, "chat_history": chat_history})
    
    chat_history.extend([
        HumanMessage(
            content=response["question"],
            response_metadata={"source_document": response["documents"]}
        ),
        response["generation"]
    ])
    
    return response["generation"], chat_history


# Example usage
if __name__ == "__main__":
    agentic_qa("How does GPT-4 work?", [])
