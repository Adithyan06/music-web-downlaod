import streamlit as st

import openai

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

    try:

        with openai.AuthClient() as client:

            ai_response = generate_response(user_input)

            st.text_area("AI:", value=ai_response, key="ai_response")

    except openai.error.AuthenticationError:

        st.error("Invalid OpenAI API key. Please check your API key.")

