import streamlit as st
from pytube import YouTube

# Function to download YouTube video as MP3
def download_mp3(url):
    try:
        st.info("Downloading... Please wait.")
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        output_path = audio_stream.download()
        st.audio(output_path, format='audio/mp3')
        st.success("Download Complete!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Streamlit UI
st.title("YouTube MP3 Downloader")
st.write("Enter the YouTube video URL below:")
video_url = st.text_input("URL:")
if st.button("Download MP3"):
    if video_url:
        download_mp3(video_url)
    else:
        st.warning("Please enter a valid YouTube URL.")

# Footer
st.write("Note: Please ensure you have the right to download and use the content from YouTube.")
        

                
