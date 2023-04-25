import os , time,random,sys
import wget
import time
import streamlit as st
import requests
from pathlib import Path
from yt_dlp import YoutubeDL
from pytube import YouTube
from utils.util import humanbytes

st.set_page_config(page_title="Download Now",page_icon="kannan/logo.png",menu_items={
    "Get help": "https://github.com/dudegladiator/YoutubeDownloader",
    "Report a bug" : "https://github.com/dudegladiator/YoutubeDownloader/issues"
    
})                       

st.cache()
st.title("Download any YouTube videos with best quality 🥳")
URL = st.text_input("Paste any YouTube URL/Link")
yt = YouTube(URL)
if(st.button('Apply')):
     ytregex = r"^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"
     if not ytregex:
         await st.write("Give me link")
         return
     z = st.info("Please Wait...")
     ydl_opts = {"outtmpl": f"{yt.title}.mp4"}
     with YoutubeDL() as ydl:
         info = ydl.extract_info(URL, download=False)
         video = ydl.prepare_filename(info)
         ydl.process_info(info)
         p = Path(video)
         p=p.rename(p.with_name(f"{yt.title[:33]}.mp4"))
         with open(p,'rb') as f:
             st.write(f"{yt.title}")
             st.video(f)
             st.download_button("Download Video 📥",data=f,file_name=f"{yt.title}.mp4") 
