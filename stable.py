import streamlit as st
import requests
import base64

# 🔴 Replace with your NEW API key
API_KEY = "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"

st.set_page_config(page_title="AI Image Generator", layout="centered")

st.title("🎨 AI Image Generator")
st.write("Generate images using NVIDIA Stable Diffusion")
st.text("Sanju monna")
prompt = st.text_input("Enter your prompt:")
aspect_ratio = st.selectbox("Select Image Ratio",["1:1", "16:9", "9:16", "4:3", "3:4"])

if st.button("Generate Image"):
    if prompt == "":
        st.warning("Please enter a prompt")
    else:
        with st.spinner("Generating image..."):

            url = "https://ai.api.nvidia.com/v1/genai/stabilityai/stable-diffusion-3-medium"

            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "authorization": f"Bearer {API_KEY}"   
            }
            data = {
                "prompt": prompt,
                "aspect_ratio": aspect_ratio,
                "cfg_scale": 5,
                "mode": "text-to-image",
                "model": "sd3",
                "output_format": "jpeg",
                "seed": 0,
                "steps": 50,
            }

            response = requests.post(url, headers=headers, json=data)

            if response.status_code == 200:
                result = response.json()
                
                if "image" in result:
                    image_base64 = result["image"] 
                    image_bytes = base64.b64decode(image_base64)
                    st.image(image_bytes, caption="Generated Image")
                    st.success("Image generated successfully!")
                    st.download_button(
                        label="📥 Download Image",
                        data=image_bytes,
                        file_name="generated_image.jpg",
                        mime="image/jpeg"
                    )
                else:
                    st.error("Invalid response")
                    st.write(result)
            else:
                st.error("Error generating image")
                st.text(response.text)
