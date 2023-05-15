import streamlit as st

import requests

from PIL import Image

API_KEY = "e4f21595-772e-41d5-ba54-67948b227d18"  # Replace with your API key

@st.cache(allow_output_mutation=True)

def get_image_from_text(text):

    url = "https://api.deepai.org/api/text2img"

    payload = {"text": text}

    headers = {"api-key": API_KEY}

    response = requests.post(url, data=payload, headers=headers)

    

    if response.status_code == 200:

        json_data = response.json()

        image_url = json_data.get("output_url")

        if image_url:

            image = Image.open(requests.get(image_url, stream=True).raw)

            return image, image_url

        else:

            raise ValueError("Failed to generate image. Please try again.")

    else:

        raise ValueError(f"An error occurred: {response.content.decode()}. Please try again.")


# Set up Streamlit app title and sidebar

st.title("Image Generation")

st.sidebar.header("Text Input")

# Get user input

text_input = st.sidebar.text_input("Enter text:", value="", key="text_input")

# Generate image from text

if st.sidebar.button("Generate Image"):

    if text_input:

        try:

            with st.spinner("Generating image..."):

                image, image_url = get_image_from_text(text_input)

        except ValueError as e:

            st.error(str(e))

        else:

            st.image(image, caption="Generated Image", use_column_width=True)

            st.markdown(f"**Image URL:** {image_url}")

            if st.button("Save Image"):

                image.save("generated_image.png")

                st.success("Image saved successfully!")

    else:

        st.warning("Please enter some text to generate an image.")

