import streamlit as st

import requests

# Function to send user message and get chatbot response

def get_chatbot_response(message):

    url = "https://simple-chatgpt-api.p.rapidapi.com/ask"
    headers = {
       "content-type": "application/json",
       "X-RapidAPI-Key": "33af2319cbmshd1a3ee767f631f3p16a1dfjsnd5800101f122",
       "X-RapidAPI-Host": "simple-chatgpt-api.p.rapidapi.com"
    }
    payload = {"question": message}

    response = requests.post(url, json=payload, headers=headers)

    return response.json()["choices"][0]["text"].strip
# Main function to create the web app

def main():

    st.title("AI Chatbot")

    # Create a list to store chat history

    chat_history = []

    # Display chat history

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

        user_input = ""

# Run the main function

if __name__ == "__main__":

    main()

