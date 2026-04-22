import streamlit as st
import requests
import base64

# 🔴 Use your NEW API key (keep it secret)
API_KEY = "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"

st.set_page_config(page_title="AI Image Generator", layout="centered")

st.title("🎨 AI Image Generator (FLUX Model)")

# 🧠 Inputs
prompt = st.text_input("Enter prompt:")

aspect_ratio = st.selectbox(
    "Select Image Ratio",
    ["1:1", "16:9", "9:16", "4:3", "3:4"]
)

# 🧮 Convert ratio → width & height
def get_dimensions(ratio):
    if ratio == "1:1":
        return 1024, 1024
    elif ratio == "16:9":
        return 1024, 576
    elif ratio == "9:16":
        return 576, 1024
    elif ratio == "4:3":
        return 1024, 768
    elif ratio == "3:4":
        return 768, 1024

if st.button("Generate Image"):

    if prompt == "":
        st.warning("Please enter a prompt")
    else:
        with st.spinner("Generating image..."):

            width, height = get_dimensions(aspect_ratio)

            url = "https://ai.api.nvidia.com/v1/genai/black-forest-labs/flux.2-klein-4b"

            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Accept": "application/json",
                "Content-Type": "application/json"
            }

            payload = {
                "prompt": prompt,
                "width": width,
                "height": height,
                "seed": 0,
                "steps": 4
            }

            response = requests.post(url, headers=headers, json=payload)

            if response.status_code == 200:
                result = response.json()
                if "artifacts" in result:
                    image_base64 = result["artifacts"][0]["base64"]
                    image_bytes = base64.b64decode(image_base64)
                    st.image(image_bytes, caption="Generated Image")
                    st.download_button(
                        label="📥 Download Image",
                        data=image_bytes,
                        file_name="generated_image.jpg",
                        mime="image/jpeg"
                    )
                    st.success("Image generated successfully!")
                else:
                   st.error("Invalid response")
                   st.write(result)
            else:
                st.error(f"Error: {response.status_code}")
                st.text(response.text)
