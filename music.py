import streamlit as st
from PIL import Image, ImageDraw, ImageFont

def generate_logo(text, font_size, text_color, bg_color, output_path):
# Create a blank image with the desired background color
    image = Image.new('RGB', (500, 500), bg_color)

    draw = ImageDraw.Draw(image)

    # Load a font (adjust the path to your font file)

    font = ImageFont.truetype("Arial.ttf", font_size)

    # Calculate the width and height of the text

    text_width, text_height = draw.textsize(text, font=font)

    # Calculate the x and y coordinates to center the text

    x = (image.width - text_width) // 2

    y = (image.height - text_height) // 2

    # Draw the text on the image

    draw.text((x, y), text, font=font, fill=text_color)

    # Save the generated logo to the output path

    image.save(output_path)

# Main function to run the Streamlit app
st.cache()
st.set_page_config(
   page_title="Download Any songs now !!",
   page_icon="random",
   menu_items={"Get help": "https://github.com/Adithyan06"}
    
st.title("Logo Generator")

    # User inputs
text = st.text_input("Enter text for the logo:")
font_size = st.slider("Select font size:", 20, 100, 50)
text_color = st.color_picker("Select text color:", "#FFFFFF")
bg_color = st.color_picker("Select background color:", "#000000")
output_path = st.text_input("Enter output path to save the logo:", "logo.png")# Generate and display the logo

if st.button("Generate Logo"):
    generate_logo(text, font_size, text_color, bg_color, output_path)
    st.success("Logo generated successfully!")
    # Display the generated logo
    st.image(output_path)
