import streamlit as st

from PIL import Image

import openai

# Set up OpenAI API credentials

openai.api_key = "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"  # Replace with your OpenAI API key

# Function to generate images from text using DALL-E

def generate_image_from_text(text):

    response = openai.Completion.create(

        engine="davinci",

        prompt=text,

        max_tokens=50,

        n=1,

        stop=None,

        temperature=0.8,

    )

    image_data = response.choices[0].image

    image = Image.open(image_data)

    return image

# Set up Streamlit app

st.title("Image Generation with DALL-E")

text_input = st.text_input("Enter text:", value="", key="text_input")

generate_image_button = st.button("Generate Image")

# Generate and display the image

if generate_image_button:

    if text_input:

        try:

            with st.spinner("Generating image..."):

                image = generate_image_from_text(text_input)

            st.image(image, caption="Generated Image", use_column_width=True)

        except Exception as e:

            st.error(f"An error occurred: {str(e)}")

    else:

        st.warning("Please enter some text.")

