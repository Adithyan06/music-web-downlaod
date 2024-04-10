from youtube_search import YoutubeSearch
import streamlit as st
import yt_dlp
import os

def download_song(song_name):
    # Download the song using youtube_dl
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'flac',
            'preferredquality': '192',
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
    results = YoutubeSearch(song_name, max_results=1).to_dict()
    title = results[0]["title"]
    if st.button('Download'):
        if song_name:
            song_file = download_song(song_name)
            if song_file:
                st.success('Download complete!')
                st.write('Here is the song:')
                audio_file = open(song_file, 'rb')
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format='audio/flac')
                st.download_button("Download 🥀",data=audio_bytes,file_name=f"{title}.flac")
            else:
                st.error('Failed to download the song.')
        else:
            st.warning('Please enter a song name.')
            

if __name__ == "__main__":
    main()
