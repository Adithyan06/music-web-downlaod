
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
    
    if st.button('Download'):
        if song_name:
            song_file = download_song(song_name)
            if song_file:
                st.success('Download complete!')
                st.write('Download the song here:')
                st.markdown(f'<a href="{song_file}" download>Download {song_file}</a>', unsafe_allow_html=True)
            else:
                st.error('Failed to download the song.')
        else:
            st.warning('Please enter a song name.')

if __name__ == "__main__":
    main()
