import streamlit as st
from pathlib import Path
from pytube import YouTube
from yt_dlp import YoutubeDL
import os
import time
import ffmpeg
from youtube_search import YoutubeSearch
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_ej2lfhv2.json")

st.cache()
st.set_page_config(page_title="Download Any songs now !!",page_icon="❤️",menu_items={
      "Get help": "https://github.com/Adithyan06"
})
# st_lottie(lottie_coding, height=300, key="download")
st.title("YouTube Videos Downloader") 
st.caption("Download any Video/Audio Songs.Just copy the name or YouTube link of the song you want 🥳")
st_lottie(lottie_coding, height=280, key="YouTube")

query = st.text_input("Song Name or YouTube URL",placeholder="Song Name")
# option = st.radio("Select Type: ", ('Audio 🎶', 'Video 🎥'))
results = YoutubeSearch(query, max_results=1).to_dict()
link=f"https://youtube.com{results[0]['url_suffix']}"
title = results[0]["title"]
yt = YouTube(link)
option = st.radio("Select Type: ", ('Audio 🎶', 'Video 🎥'))

if (option == 'Video 🎥'):
   res = st.selectbox("Select The resolution",("720p","360p","144p"))                
   video = yt.streams.get_by_itag(yt.streams.filter(res=res , progressive="True" )[0].itag)      
   hi = video.download()           
   p = Path(hi)
   p=p.rename(p.with_name(f"{yt.title[:35]}.mp4"))
   if(st.button('Submit')):
        with st.spinner('Wait for it...'):
            with open(p,'rb' ) as f:                
                st.write(f"{yt.title}")
                st.video(f)
                st.write("Link -", link)
                st.download_button("Save Video", data=f, file_name=f"{title[:35]}.mp4") 
else:                 
     audio = yt.streams.get_by_itag(yt.streams.filter(type="audio",mime_type="audio/webm")[0].itag) 
     a = audio.download()
     ma = Path(a)
     ma=ma.rename(ma.with_name(f"{title[:33]}.mp3"))  
     if(st.button('Submit')): 
          with st.spinner('Wait for it...'):
               with open(ma,'rb' ) as s:                
                   st.write(f"{title[:33]}")
                   st.audio(s)
                   st.download_button("Save Audio", data=s, file_name=f"{yt.title[:33]}.mp3")  
