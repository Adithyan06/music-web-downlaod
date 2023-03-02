import os , time,random,sys
import streamlit as st
from pathlib import Path
import os
import ffmpeg
import subprocess
from typing import List
import uuid
import traceback

st.cache()
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


# From here Website start
st.set_page_config(page_title="Download Songs Now",page_icon="images/logo.png",menu_items={
    "Get help": "https://github.com/dudegladiator/YoutubeDownloader",
    "Report a bug" : "https://github.com/dudegladiator/YoutubeDownloader/issues"
    
})
st.title("Download song from spotify") 
query = st.text_input("Spotify url")
if(st.button('Submit')):
     result = query.title()
     st.info(result)     
     download_path = os.getcwd() + "/" + str(uuid.uuid4())
     try:
         spotdl.download_from_spotify(download_path, query)
         spotdl.send_songs_from_directory(download_path)
     except Exception as e:
         print(e)
         st.warning("not found")
