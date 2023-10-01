# Import necessary libraries
import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"

# Streamlit app title and description
st.title("Image Generator from Prompt")
st.write("Enter a prompt and generate an image!")

# User input: prompt
prompt = st.text_input("Enter your prompt:", "A colorful sunset over the mountains")

# Function to generate image based on prompt using OpenAI's DALL-E API
def generate_image(prompt):
    try:
        # Generate image using DALL-E API
        response = openai.Image.create(prompt=prompt, n=1)
        # Get the image URL from the API response
        image_url = response.data[0]["url"]
        # Display the generated image
        st.image(image_url, caption="Generated Image", use_column_width=True)
    except Exception as e:
        # Display an error message if image generation fails
        st.error(f"Image generation failed: {str(e)}")

# Button to generate image when clicked
if st.button("Generate Image"):
    generate_image(prompt)
        
