import streamlit as st
import requests
import base64

# 🔴 Replace with your NEW API key
API_KEY = "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"

st.set_page_config(page_title="AI Image Generator", layout="centered")

st.title("🎨 AI Image Generator")
st.write("Generate images using NVIDIA Stable Diffusion")

prompt = st.text_input("Enter your prompt:")

if st.button("Generate Image"):
    if prompt == "":
        st.warning("Please enter a prompt")
    else:
        with st.spinner("Generating image..."):

            url = "https://ai.api.nvidia.com/v1/genai/stabilityai/stable-diffusion-3-medium"

            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }

            data = {
                "prompt": prompt,
                "model": "stabilityai/stable-diffusion-xl",
                "width": 1024,
                "height": 1024
            }

            response = requests.post(url, headers=headers, json=data)

            if response.status_code == 200:
                result = response.json()

                image_base64 = result["data"][0]["b64_json"]
                image_bytes = base64.b64decode(image_base64)

                st.image(image_bytes, caption="Generated Image", use_column_width=True)
                st.success("Image generated successfully!")
            else:
                st.error("Error generating image")
                st.text(response.text)
