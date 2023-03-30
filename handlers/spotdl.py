import os
import ffmpeg
import subprocess
from typing import List
import streamlit as st
from yt_dlp import YoutubeDL

def download_from_spotify(download_path: str, query: List[str]):
    os.mkdir(download_path)
    os.chdir(download_path)
    os.system(f'spotdl {query}')
    os.chdir("..")

def send_songs_from_directory(
    directory_path: str,query):
    directory = os.listdir(directory_path)
    for file in directory:
        if not file.endswith(".mp3"):
            continue
        try:
            st.write(f"{file}")
            st.audio(open(f'{directory_path}/{file}', 'rb'))
            st.download_button(label='Save Audio', data=(open(f'{directory_path}/{file}', 'rb')),file_name=f"{file}")
        except Exception:
            st.write("Note Found")
    
    subprocess.run(['ffmpeg','-r', directory_path])  

@sync_to_async
def getIds(video):
    ids = []
    with YoutubeDL({'quiet':True}) as ydl:
        info_dict = ydl.extract_info(video, download=False)
        try:
            info_dict = info_dict['entries']
            ids.extend([x.get('id'),x.get('playlist_index'),x.get('creator') or x.get('uploader'),x.get('title'),x.get('duration'),x.get('thumbnail')] for x in info_dict)
        except:
            ids.append([info_dict.get('id'),info_dict.get('playlist_index'),info_dict.get('creator') or info_dict.get('uploader'),info_dict.get('title'),info_dict.get('duration'),info_dict.get('thumbnail')])
    return ids 
