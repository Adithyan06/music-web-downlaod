import streamlit as st
from pathlib import Path
from pytube import YouTube
import os , time,random,sys
import time
import yt_dlp
from youtube_search import YoutubeSearch

st.cache()
st.set_page_config(page_title="Download Now",page_icon="images/logo.png",menu_items={
    "Get help": "https://github.com/dudegladiator/YoutubeDownloader",
    "Report a bug" : "https://github.com/dudegladiator/YoutubeDownloader/issues"
    
})

def download (query,res):
    st.title("Download Youtube Video")
    query=st.text_input("Youtube Video or Playlist URL")
    ydl_opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
            "outtmpl": "%(alt_title)s.mp3",
            "quiet": True,
            "logtostderr": False,
    }
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            title = results[0]["title"]
        except Exception:
            st.info("Song not found")
            return
    except Exception:
        st.info("not found")
        return
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)

            a=st.button("Start Downloading 🙂")  
            st.audio(audio)
            st.download_button("Save Audio",audio,file_name=f"{title}.mp3")
