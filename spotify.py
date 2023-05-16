import streamlit as st
from pathlib import Path
import yt_dlp
from youtube_search import YoutubeSearch



# Streamlit app

st.title("Song Downloader")

# Input field for YouTube URL

url = st.text_input("Enter the YouTube URL:", value='', key='youtube_url')
youtube_url = YoutubeSearch(url, max_results=1).to_dict()
link = f"https://youtube.com{youtube_url[0]['url_suffix']}" 

            

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

                info = ydl.extract_info(link, download=False)
                audio = ydl.prepare_filename(info)
                ydl.process_info(info)
                
                video_title = info['title']
                st.info(f"Downloading '{video_title}'...")
                x = Path(audio)
                x=x.rename(x.with_name(f"{video_title}.mp3"))
                with open(x,'rb') as xx:
                    st.audio(xx)
                    st.download_button("Download 🥀",data=xx,file_name=f"{video_title}.mp3")
                    st.success("Song downloaded successfully.")

        except Exception as e:

            st.error(f"An error occurred: {str(e)}")

    else:

        st.warning("Please enter a YouTube URL.")

