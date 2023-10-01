# Import necessary libraries
import requests
import streamlit as st

# Set your DeepAI API key
deepai_api_key = "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"

# Streamlit app title and description
st.title("Image Generator from Prompt")
st.write("Enter a prompt and generate an image!")

# User input: prompt
prompt = st.text_input("Enter your prompt:", "A colorful sunset over the mountains")

# Function to generate image based on prompt using DeepAI API
def generate_image(prompt):
    try:
        # DeepAI API endpoint
        api_endpoint = "https://api.deepai.org/api/text2img"
        # Make a POST request to the API with the prompt
        response = requests.post(api_endpoint, data={"text": prompt}, headers={"api-key": deepai_api_key})
        # Check if the request was successful
        if response.status_code == 200:
            # Get the image URL from the API response
            response_data = response.json()
            image_url = response_data["output_url"]
            # Display the generated image
            st.image(image_url, caption="Generated Image", use_column_width=True)
        else:
            # Display an error message if image generation fails
            st.error("Image generation failed. Please try a different prompt.")
    except Exception as e:
        # Display an error message if there is an exception
        st.error(f"Error: {str(e)}")

# Button to generate image when clicked
if st.button("Generate Image"):
    generate_image(prompt)
        
