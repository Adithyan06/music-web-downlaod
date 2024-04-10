from youtube_search import YoutubeSearch
import streamlit as st
import yt_dlp
import os

@st.cache(allow_output_mutation=True)
def download_song(song_name):
    # Download the song using youtube_dl
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'flac',
            'preferredquality': '128',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch1:{song_name}"])

    # Find the downloaded file
    for file in os.listdir('.'):
        if file.endswith('.flac'):
            return file

def main():
    st.title('Song Downloader')
    st.write('Enter the name of the song you want to download in FLAC format:')

    song_name = st.text_input('Song Name')
    
    if st.button('Download'):
        if song_name:
          song_file = download_song(song_name)
          if song_file:
              st.success('Download complete!')
              st.write('Here is the song:')
              audio_file = open(song_file, 'rb')
              audio_bytes = audio_file.read()
              st.audio(audio_bytes, format='audio/flac')
              st.download_button("Download 🥀",data=audio_bytes)
          else:
              st.error('Failed to download the song!')
if __name__ == "__main__":
    main()
