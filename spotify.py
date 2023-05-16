import streamlit as st

import yt_dlp

# Streamlit app

st.title("Song Downloader")

# Input field for YouTube URL

youtube_url = st.text_input("Enter the YouTube URL:", value='', key='youtube_url')

# Button for downloading the song

if st.button("Download"):

    if youtube_url:

        try:

            # Configure options for downloading the audio

            ydl_opts = {

                'format': 'bestaudio/best',

                'postprocessors': [{

                    'key': 'FFmpegExtractAudio',

                    'preferredcodec': 'mp3',

                    'preferredquality': '192',

                }],

            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:

                info = ydl.extract_info(youtube_url, download=False)

                video_title = info['title']

                st.info(f"Downloading '{video_title}'...")

                ydl.download([youtube_url])

                st.success("Song downloaded successfully.")

        except Exception as e:

            st.error(f"An error occurred: {str(e)}")

    else:

        st.warning("Please enter a YouTube URL.")

