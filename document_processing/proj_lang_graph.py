#!/usr/bin/env python
# coding: utf-8

"""
Agentic RAG Flow Implementation

This script implements a Retrieval-Augmented Generation (RAG) workflow using a state graph.
It retrieves documents from a vector store, grades their relevance, optionally performs web search,
and generates an answer using an LLM. The workflow is designed to handle contextual queries
with chat history awareness.
"""

# --- Imports ---
import sys
import os
from typing import List
from typing_extensions import TypedDict
from langchain_core.output_parsers import StrOutputParser
from operator import itemgetter
from langchain.docstore.document import Document
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

# Add parent directory to sys.path for module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Custom module imports
from app_config.open_ai_cred import OPENAI_KEY, TAVILY_API_KEY, WEATHER_API_KEY, MODEL_NAME, EMBED_MODEL
from document_processing.doc_indexer import VectorStore
from document_processing.proj_chains import query_re_writer_agent, context_qa_chain, document_grader_agent

# --- Environment Setup ---
os.environ['OPENAI_API_KEY'] = OPENAI_KEY
os.environ['TAVILY_API_KEY'] = TAVILY_API_KEY

# --- Vector Store Initialization ---
vector_store = VectorStore(MODEL_NAME, EMBED_MODEL)
chroma_db = vector_store.vectord_db_loader()

# --- State Definition ---
class GraphState(TypedDict):
    """
    Represents the state of the agentic RAG graph workflow.

    Attributes:
        question (str): The user's input question.
        generation (str): The LLM-generated response.
        web_search_needed (str): Flag indicating if web search is required ('Yes' or 'No').
        documents (List[str]): List of retrieved context documents.
        chat_history (List[str]): List of prior chat interactions for context.
    """
    question: str
    generation: str
    web_search_needed: str
    documents: List[str]
    chat_history: List[str]

# --- Helper Functions ---
def retriever_call():
    """
    Creates and returns a similarity threshold retriever from the vector store.

    Returns:
        Retriever: A configured retriever object for document retrieval.
    """
    similarity_threshold_retriever = chroma_db.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"k": 3, "score_threshold": 0.3}
    )
    return similarity_threshold_retriever

# --- Workflow Nodes ---
def retrieve(state: GraphState) -> GraphState:
    """
    Retrieves documents from the vector store based on the input question.

    Args:
        state (GraphState): Current state containing the question and chat history.

    Returns:
        GraphState: Updated state with retrieved documents.
    """
    print("---RETRIEVAL FROM VECTOR DB---")
    question = state["question"]
    chat_history = state['chat_history']
    retriever = retriever_call()
    documents = retriever.invoke(question)
    return {
        "documents": documents,
        "question": question,
        "chat_history": chat_history
    }

def grade_documents(state: GraphState) -> GraphState:
    """
    Grades the relevance of retrieved documents to the question using an LLM grader.

    If any document is irrelevant or no documents are retrieved, sets web_search_needed to 'Yes'.
    Filters out irrelevant documents.

    Args:
        state (GraphState): Current state with question and documents.

    Returns:
        GraphState: Updated state with filtered documents and web search flag.
    """
    print("---CHECK DOCUMENT RELEVANCE TO QUESTION---")
    question = state["question"]
    documents = state["documents"]
    doc_grader = document_grader_agent()
    filtered_docs = []
    web_search_needed = "No"

    if documents:
        for doc in documents:
            score = doc_grader.invoke({"question": question, "document": doc.page_content})
            grade = score.binary_score
            if grade == "yes":
                print("---GRADE: DOCUMENT RELEVANT---")
                filtered_docs.append(doc)
            else:
                print("---GRADE: DOCUMENT NOT RELEVANT---")
                web_search_needed = "Yes"
    else:
        print("---NO DOCUMENTS RETRIEVED---")
        web_search_needed = "Yes"

    return {
        "documents": filtered_docs,
        "question": question,
        "web_search_needed": web_search_needed,
        "chat_history": state['chat_history']
    }

def rewrite_query(state: GraphState) -> GraphState:
    """
    Rewrites the input question to improve its clarity or relevance using an LLM agent.

    Args:
        state (GraphState): Current state with the original question.

    Returns:
        GraphState: Updated state with a rewritten question.
    """
    print("---REWRITE QUERY---")
    question = state["question"]
    documents = state["documents"]
    question_rewriter = query_re_writer_agent()
    better_question = question_rewriter.invoke({"question": question})
    return {
        "documents": documents,
        "question": better_question,
        "chat_history": state['chat_history']
    }

def web_search(state: GraphState) -> GraphState:
    """
    Performs a web search using the rewritten question and appends results to documents.

    Args:
        state (GraphState): Current state with question and existing documents.

    Returns:
        GraphState: Updated state with web search results added to documents.
    """
    print("---WEB SEARCH---")
    question = state["question"]
    documents = state["documents"]
    final_retriever = retriever_call()
    docs = final_retriever.invoke(question)
    web_results = "\n\n".join([d.page_content for d in docs])
    web_results_doc = Document(page_content=web_results)
    documents.append(web_results_doc)
    return {
        "documents": documents,
        "question": question,
        "chat_history": state['chat_history']
    }

def generate_answer(state: GraphState) -> GraphState:
    """
    Generates an answer from the context documents using an LLM-based RAG chain.

    Args:
        state (GraphState): Current state with question and documents.

    Returns:
        GraphState: Updated state with the generated answer.
    """
    print("---GENERATE ANSWER---")
    question = state["question"]
    documents = state["documents"]
    chatgpt = ChatOpenAI(model_name=MODEL_NAME, temperature=0)
    final_retriever = retriever_call()
    rag_chain = context_qa_chain(chatgpt, final_retriever)
    generation = rag_chain.invoke({"input": question, "chat_history": state['chat_history']})
    return {
        "documents": documents,
        "question": question,
        "generation": generation["answer"],
        "chat_history": state['chat_history']
    }

def decide_to_generate(state: GraphState) -> str:
    """
    Decides whether to generate an answer or rewrite the query based on document relevance.

    Args:
        state (GraphState): Current state with web_search_needed flag.

    Returns:
        str: Next node to execute ('rewrite_query' or 'generate_answer').
    """
    print("---ASSESS GRADED DOCUMENTS---")
    web_search_needed = state["web_search_needed"]
    if web_search_needed == "Yes":
        print("---DECISION: SOME or ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, REWRITE QUERY---")
        return "rewrite_query"
    else:
        print("---DECISION: GENERATE RESPONSE---")
        return "generate_answer"

# --- Graph Construction ---
def agentic_rag_flow():
    """
    Constructs and compiles the agentic RAG workflow as a state graph.

    Returns:
        Compiled StateGraph: The configured RAG workflow.
    """
    from langgraph.graph import END, StateGraph
    
    # Initialize the state graph
    agentic_rag = StateGraph(GraphState)

    # Add nodes to the graph
    agentic_rag.add_node("retrieve", retrieve)
    agentic_rag.add_node("grade_documents", grade_documents)
    agentic_rag.add_node("rewrite_query", rewrite_query)
    agentic_rag.add_node("web_search", web_search)
    agentic_rag.add_node("generate_answer", generate_answer)

    # Define the workflow edges
    agentic_rag.set_entry_point("retrieve")
    agentic_rag.add_edge("retrieve", "grade_documents")
    agentic_rag.add_conditional_edges(
        "grade_documents",
        decide_to_generate,
        {"rewrite_query": "rewrite_query", "generate_answer": "generate_answer"}
    )
    agentic_rag.add_edge("rewrite_query", "web_search")
    agentic_rag.add_edge("web_search", "generate_answer")
    agentic_rag.add_edge("generate_answer", END)

    # Compile the graph
    return agentic_rag.compile()

# # --- Main Execution (if run as script) ---
# if __name__ == "__main__":
#     # Example usage (not part of original logic, added for demonstration)
#     rag_workflow = agentic_rag_flow()
#     initial_state = {
#         "question": "What is the weather like today?",
#         "generation": "",
#         "web_search_needed": "No",
#         "documents": [],
#         "chat_history": []
#     }
#     result = rag_workflow.invoke(initial_state)
#     print(result)