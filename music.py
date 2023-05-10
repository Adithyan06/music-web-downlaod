import streamlit as st

from pytube import YouTube

# Streamlit app title and description

st.title("YouTube Video Downloader")

st.markdown("Download YouTube videos in different qualities")

# Get YouTube video URL from user

video_url = st.text_input("Enter YouTube video URL:", "")

# Check if the user has entered a valid YouTube video URL

if video_url:

    try:

        # Create a YouTube object from the video URL

        yt = YouTube(video_url)

        # Display video details

        st.subheader("Video Details:")

        st.write("Title:", yt.title)

        st.write("Author:", yt.author)

        st.write("Duration:", yt.length, "seconds")

        # Get available video streams

        streams = yt.streams.filter(progressive=True)

        # Display available video qualities

        st.subheader("Available Qualities:")

        for stream in streams:

            st.write(f"Quality: {stream.resolution}, Format: {stream.mime_type}")

        # Allow user to select desired video quality

        selected_quality = st.selectbox("Select Video Quality:", options=[stream.resolution for stream in streams])

        # Find the selected video stream

        selected_stream = next(stream for stream in streams if stream.resolution == selected_quality)

        # Display download button

        if st.button("Download"):

            # Download the selected video stream

            selected_stream.download()

            st.success("Video downloaded successfully!")

    except Exception as e:

        st.error("Error: Invalid YouTube URL or unable to fetch video details.")

        st.error(str(e))

