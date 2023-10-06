import openai
import streamlit as st

# Set your OpenAI API key here
openai.api_key = "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"

# Streamlit app title and description
st.title("Advanced Chatbot with GPT-3.5")
st.write("Enter your message below and the chatbot will respond!")

# User input: text box for entering messages
user_input = st.text_input("You:", "")

# Function to generate chatbot response using OpenAI's GPT-3.5 API
def generate_response(input_text):
    # Use the OpenAI API to generate a response based on user input
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the text-davinci-003 engine (GPT-3.5)
        prompt=input_text,
        max_tokens=150,  # Limit the response length
        n=1,  # Generate only 1 response
    )
    # Get the generated response from the API
    bot_response = response.choices[0].text.strip()
    return bot_response

# Button to generate chatbot response when clicked
if st.button("Send"):
    # Get chatbot response based on user input
    bot_response = generate_response(user_input)
    # Display chatbot response
    st.text_area("Chatbot:", value=bot_response, height=200)

st.write("have a nice day ☺️")
