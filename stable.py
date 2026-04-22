import streamlit as st
import requests
import base64

# 🔴 Replace with your NEW API key
API_KEY = "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"

st.set_page_config(page_title="AI Image Generator", layout="centered")

st.title("🎨 AI Image Generator")
st.write("Generate images using NVIDIA Stable Diffusion")
prompt = st.text_input("Enter your prompt:")
aspect_ratio = st.selectbox("Select Image Ratio",["1:1","16:9","9:16","5:4","4:5","3:2","2:3"])

if st.button("Generate Image"):
    if prompt == "":
        st.warning("Please enter a prompt")
    else:
        with st.spinner("Generating image..."):

            url = "https://ai.api.nvidia.com/v1/genai/black-forest-labs/flux.2-klein-4b"

            headers = {
                "Accept": "application/json",
                "Authorization": f"Bearer {API_KEY}"   
            }
            data = {
                     "prompt": prompt,
                     "width": 1024,
                     "height": 1024,
                     "seed": 0,
                     "steps": 4
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
