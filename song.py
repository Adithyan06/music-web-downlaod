import streamlit as st
from pytube import YouTube

# Set the title of the web app
st.title("YouTube Song Downloader")

# Input field for YouTube URL
youtube_url = st.text_input("Enter the URL of the YouTube video:")

if youtube_url:
    try:
        # Fetch YouTube video object
        yt = YouTube(youtube_url)
        
        # Display video information
        st.write(f"**Title**: {yt.title}")
        st.write(f"**Length**: {yt.length // 60} minutes {yt.length % 60} seconds")
        st.write(f"**Views**: {yt.views}")
        
        # Fetch available audio streams
        audio_streams = yt.streams.filter(only_audio=True)
        
        # Allow user to select audio quality
        stream = st.selectbox("Choose an audio stream:", [f"{s.abr} - {s.mime_type}" for s in audio_streams])
        
        # Button to download the selected stream
        if st.button("Download"):
            # Extract the selected stream
            selected_stream = audio_streams.get_by_itag(audio_streams[int(stream.split(' ')[0])].itag)
            
            # Download the audio file
            audio_file = selected_stream.download(filename=f"{yt.title}.mp3")
            
            # Confirm download success and provide download link
            st.success(f"Downloaded: {yt.title}")
            st.write(f"[Click here to download the file](./{audio_file})")
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
