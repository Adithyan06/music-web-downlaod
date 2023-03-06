import streamlit as st
from pathlib import Path
from pytube import YouTube
from yt_dlp import YoutubeDL
from random import randint
import os, random, sys
import time
import ffmpeg
import uuid
from youtube_search import YoutubeSearch

async def download_songs(query):
    ydl_opts = {
        'format': "bestaudio/best",
        'default_search': 'ytsearch',
        'noplaylist': True,
        "nocheckcertificate": True,
        "outtmpl": "%(title)s.mp3",
        "quiet": True,
        "addmetadata": True,
        "prefer_ffmpeg": True,
        "geo_bypass": True,

        "nocheckcertificate": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            video = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]['id']
            info = ydl.extract_info(video)
            filename = ydl.prepare_filename(info)
            if not filename:
               st.write("Track Not Found⚠️")
            else:
                path_link = filename
                return path_link
        except Exception as e:
            pass
            st.write(e)
    return video 

st.cache()
st.set_page_config(page_title="Download Any songs now !!",page_icon="images/logo.png",menu_items={
      "Get help": "https://github.com/Adithyan06"
})

st.title("Download any Songs You Want 🤩") 
st.caption("Download any Video/Audio Songs.Just copy the name or YouTube link of the song you want 🥳")

query = st.text_input("Song Name or YouTube URL",placeholder="Song Name")
option = st.radio("Select Type: ", ('Audio 🎶', 'Video 🎥'))
try:
      results = []
      count = 0
      while len(results) == 0 and count < 6:
          if count>0:
              time.sleep(0.5)
          results = YoutubeSearch(query, max_results=1).to_dict()
          count += 1
      try:
          link = f"https://youtube.com{results[0]['url_suffix']}"
          title = results[0]["title"]
          yt = YouTube(link)
          if (option == 'Video 🎥'):
                res = st.selectbox("Select The resolution",("720p","360p","144p"))
                if(st.button('Submit')):
                     st.info("Please Wait....")
                     video = yt.streams.get_by_itag(yt.streams.filter(res=res , progressive="True" )[0].itag)      
                     hi = video.download()           
                     p = Path(hi)
                     p=p.rename(p.with_name(f"{yt.title[:33]}.mp4"))
                     with open(p,'rb' ) as f:                
                         st.write(f"{yt.title}")
                         st.video(f)
                         st.download_button("Save Video", data=f, file_name=f"{title[:33]}.mp4") 
          else:
               if(st.button('Submit')):
                   st.info("Please Wait....")
                   bla=download_songs(query)
#                  audio = yt.streams.get_by_itag(yt.streams.filter(type="audio",mime_type="audio/webm")[0].itag)
#                  a = audio.download()
#                  ma = Path(bla)
#                  ma=ma.rename(ma.with_name(f"{title[:33]}.mp3"))   
#                  with open(ma,'rb' ) as s:                
                   st.write(f"{title[:33]}")
                   st.audio(bla)
                   st.download_button("Save Audio", data=bla, file_name=f"{yt.title[:33]}.mp3")     
      except Exception as e:
          st.info("Song not found")
          st.write(e)
except Exception:
    st.info("not found")
