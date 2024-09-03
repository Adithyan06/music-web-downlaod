import streamlit as st
from pathlib import Path
import requests 
from yt_dlp import YoutubeDL
from pytube import YouTube
from youtube_search import YoutubeSearch
from savify import Savify
from savify.types import Type, Format, Quality

s = Savify(api_credentials=("b1dcbb0c6d0f452f9f01710440ffce9c","2b01cc24bb674e87a18d773e671c8660"))

st.set_page_config(page_title="Download Now",page_icon="🧡",menu_items={
    "Get help": "https://github.com/dudegladiator/YoutubeDownloader",
    "Report a bug" : "https://github.com/dudegladiator/YoutubeDownloader/issues"
    
})                       
st.cache()
st.title("Download any YouTube videos with best quality 🥳")

URL = st.text_input("Paste any YouTube URL/Link",placeholder="Enter Name/URL")
option = st.radio("Select Type: ", ('YouTube', 'URL Upload', 'Spotify'))
if(st.button('Apply')):
     with st.spinner('Downloading...'):
         if (option == 'YouTube'):
            ydl_opts = {
                        "format": "bv+ba/b",
                        "addmetadata": True,
                        "key": "FFmpegMetadata",
                        "prefer_ffmpeg": True,
                        "geo_bypass": True,
                        "nocheckcertificate": True,
                        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
                        "outtmpl": "%(title)s.mp4",
                        "logtostderr": False,
                        "quiet": True
            }
            results = YoutubeSearch(URL, max_results=1).to_dict()
            link=f"https://youtube.com{results[0]['url_suffix']}"
            title = results[0]["title"]
            yt = YouTube(link, '-f mp4')
            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(link, download=False)
                video = ydl.prepare_filename(info)
                ydl.process_info(info)
                p = Path(video)
                p=p.rename(p.with_name(f"{title}.mp4"))
                with open(p,'rb') as f:
                    st.write(f"{title}")
                    st.video(f)
                    st.download_button("Download Video 📥",data=f)
         if (option == 'URL Upload'):
              with YoutubeDL() as ydl:
                  info = ydl.extract_info(URL, download=False)
                  video = ydl.prepare_filename(info)
                  ydl.process_info(info)
                  x = Path(video)
                  x=x.rename(x.with_name(f"{video}.mp4"))
                  with open(x,'rb') as xx:
                      st.write(video)
                      st.video(xx)
                      st.download_button("Download 🥀",data=xx,file_name=f"{video}.mp4")
         else:            
             song = s.download(f"{URL}", query_type=Type.TRACK)
             st.song(song)
