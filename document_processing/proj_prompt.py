import os
from app_config.open_ai_cred import OPENAI_KEY, TAVILY_API_KEY
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Set environment variables
os.environ['OPENAI_API_KEY'] = OPENAI_KEY
os.environ['TAVILY_API_KEY'] = TAVILY_API_KEY

# Contextual Question Reformulation Prompt
CONTEXTUALIZE_Q_SYSTEM_PROMPT = """Given a chat history and the latest user question \
which might reference context in the chat history, formulate a standalone question \
which can be understood without the chat history. Do NOT answer the question, \
just reformulate it if needed and otherwise return it as is."""

contextualize_q_prompt = ChatPromptTemplate.from_messages([
    ("system", CONTEXTUALIZE_Q_SYSTEM_PROMPT),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
])

# QA System Prompt
QA_SYSTEM_PROMPT = """You are an assistant for question-answering tasks. \
Use the following pieces of retrieved context to answer the question. \
Use three sentences maximum and keep the answer concise. \
If you don't know the answer, just say that you don't know. Do not generate any answer if it's not present in the context.\
{context}"""

qa_prompt = ChatPromptTemplate.from_messages([
    ("system", QA_SYSTEM_PROMPT),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
])

# Query Rewriting Prompt
SYS_PROMPT_RW = """Act as a question re-writer and perform the following task:
- Convert the following input question to a better version that is optimized for web search.
- When re-writing, look at the input question and try to reason about the underlying semantic intent / meaning."""

re_write_prompt = ChatPromptTemplate.from_messages([
    ("system", SYS_PROMPT_RW),
    ("human", """Here is the initial question:
                 {question}
                 
                 Formulate an improved question.
              """),
])

# Document Grading Prompt
SYS_PROMPT_GRADE = """You are an expert grader assessing relevance of a retrieved document to a user question.
Follow these instructions for grading:
- If the document contains keyword(s) or semantic meaning related to the question, grade it as relevant.
- Your grade should be either 'yes' or 'no' to indicate whether the document is relevant to the question or not."""

grade_prompt = ChatPromptTemplate.from_messages([
    ("system", SYS_PROMPT_GRADE),
    ("human", """Retrieved document:
                 {document}
                 
                 User question:
                 {question}
              """),
])
