import streamlit as st

import requests

# Function to send user message and get chatbot response

def get_chatbot_response(message):

    url = "https://api.openai.com/v1/engines/davinci-codex/completions"

    headers = {

        "Authorization": "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",

        "Content-Type": "application/json",

    }

    data = {

        "prompt": message,

        "max_tokens": 50,

    }

    response = requests.post(url, json=data, headers=headers)

    return response.json()["choices"][0]["text"].strip()

# Main function to create the web app
st.cache()
st.set_page_config(
   page_title="Download Any songs now !!",
   page_icon="random",
   menu_items={"Get help": "https://github.com/Adithyan06"})

st.title("AI Chatbot")
chat_history = []
if len(chat_history) > 0:

    st.text("\n".join(chat_history))

    # Create a text input for the user to enter messages

    user_input = st.text_input("User:", "")

    # Check if the user has entered a message

    if user_input:

        # Add user message to the chat history

        chat_history.append("User: " + user_input)

        # Get chatbot response

        chatbot_response = get_chatbot_response(user_input)

        # Add chatbot response to the chat history

        chat_history.append("Chatbot: " + chatbot_response)

        # Clear the user input

        user_input = ""# Run the main func
