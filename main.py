import streamlit as st
from pathlib import Path
from pytube import YouTube
import os , time,random,sys
import time
import wget
import yt_dlp
from youtube_search import YoutubeSearch

st.cache()
st.set_page_config(page_title="Download Now or later",page_icon="images/logo.png",menu_items={
    "Get help": "https://github.com/dudegladiator/YoutubeDownloader",
    "Report a bug" : "https://github.com/dudegladiator/YoutubeDownloader/issues"
    
})

st.title("Download Youtube Audio")
query = st.text_input("Youtube Video or Playlist URL")

if(st.button('Submit')):
     ydl_opts = {
             "format": "bv+ba/b",
             "addmetadata": True,
             "key": "FFmpegMetadata",
             "prefer_ffmpeg": True,
             "geo_bypass": True,
             "nocheckcertificate": True,
             "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
             "outtmpl": "%(alt_title)s.mp4",
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
             yt = YouTube(link)
             audio = yt.streams.get_by_itag(yt.streams.filter(type="audio",mime_type="audio/webm")[0].itag)
             a = audio.download()
         except Exception:
             st.info("Song not found")
     except Exception:
         st.info("not found")
     try:
         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
             info_dict = ydl.extract_info(link, download=False)
             audios = ydl.prepare_filename(info_dict)
             ydl.process_info(info_dict)
             v = ydl.download(link)
             st.video(v)
             st.download_button("Save Audio",a,file_name=f"{title}.mp4") 
     except Exception:
             st.write("Song not found")
