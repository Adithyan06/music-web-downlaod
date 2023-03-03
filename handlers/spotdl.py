import os
import ffmpeg
import subprocess
from typing import List
import streamlit as st

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
            st.audio(open(f'{directory_path}/{file}', 'rb'))
        except Exception:
            st.write("Note Found")
    
    subprocess.run(['rm', '-r', directory_path])  

