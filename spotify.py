import streamlit as st

import openai

# Set up OpenAI API credentials

openai.api_key = "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"

# Set up Streamlit app title and sidebar

st.title("AI Chat")

st.sidebar.header("User Input")

# Get user input

user_input = st.sidebar.text_input("You:", value="", key="user_input")

# Define AI response function

def generate_response(user_input):

    response = openai.Completion.create(

        engine="davinci",

        prompt=user_input,

        max_tokens=50,

        temperature=0.7,

        n=1,

        stop=None,

        frequency_penalty=0.0,

        presence_penalty=0.0

    )

    return response.choices[0].text.strip()

# Generate AI response

if st.sidebar.button("Send"):

    ai_response = generate_response(user_input)

    st.text_area("AI:", value=ai_response, key="ai_response")

