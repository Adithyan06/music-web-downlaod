import streamlit as st

from chatterbot import ChatBot

from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance

chatbot = ChatBot('My Chatbot')

# Create a new trainer for the chatbot

trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot with some example data

trainer.train('chatterbot.corpus.english.greetings',

              'chatterbot.corpus.english.conversations')

# Define the Streamlit web app
st.title('AI Chatbot')

    # Get user input
user_input = st.text_input('You:', '')

    # Get chatbot response

response = chatbot.get_response(user_input)

    # Display chatbot response
st.text_area('Chatbot:', value=str(response))
