import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from document_processing.doc_qa import agentic_qa

# Initialize session state variables
def initialize_session():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "conv_history" not in st.session_state:
        st.session_state.conv_history = []

def chatbot_response(user_input):
    """Generates chatbot response using agentic_qa."""
    answer, conv = agentic_qa(user_input, st.session_state.conv_history)
    return answer

def submit_chat():
    """Handles user input, updates chat history, and clears input field."""
    user_input = st.session_state.user_input.strip()
    if user_input:
        bot_response = chatbot_response(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", bot_response))
        st.session_state.user_input = ""  # Clear input field

def display_chat():
    """Displays chat history in a scrollable text box."""
    chat_box_style = """
    <div style="height: 300px; overflow-y: auto; border: 1px solid #ddd; padding: 10px;">
    """
    chat_box_content = "".join(
        f"<p><strong>{speaker}:</strong> {message}</p>" if speaker == "You" else f"<p>{speaker}: {message}</p>"
        for speaker, message in st.session_state.chat_history
    )
    st.markdown(chat_box_style + chat_box_content + "</div>", unsafe_allow_html=True)

def main():
    """Main function to run the Streamlit chatbot application."""
    st.title("Chatbot with Streamlit")
    initialize_session()
    display_chat()
    st.text_input("Ask a question:", "", key="user_input", on_change=submit_chat, placeholder="Type your message and press Enter...")

if __name__ == "__main__":
    main()