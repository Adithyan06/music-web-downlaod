import streamlit as st

from chatterbot import ChatBot

from chatterbot.trainers import ChatterBotCorpusTrainer

def train_chatbot():

    chatbot = ChatBot('My Chatbot')

    trainer = ChatterBotCorpusTrainer(chatbot)

    trainer.train('chatterbot.corpus.english.greetings',

                  'chatterbot.corpus.english.conversations')

    return chatbot

def get_bot_response(chatbot, user_input):

    response = chatbot.get_response(user_input)

    return response

# Main function to run the Streamlit app
st.cache()
st.set_page_config(
   page_title="Download Any songs now !!",
   page_icon="random",
   menu_items={"Get help": "https://github.com/Adithyan06"})
   
chatbot = train_chatbot()
st.title("AI Chatbot")
user_input = st.text_input("User Input:")
if st.button("Send"):
  bot_response = get_bot_response(chatbot, user_input)
  st.text_area("Bot Response:", value=bot_response)
