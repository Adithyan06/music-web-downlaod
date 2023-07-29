import streamlit as st
from pathlib import Path
import time
from yt_dlp import YoutubeDL
from pytube import YouTube
from youtube_search import YoutubeSearch

st.set_page_config(page_title="Download Now",page_icon="🧡",menu_items={
    "Get help": "https://github.com/dudegladiator/YoutubeDownloader",
    "Report a bug" : "https://github.com/dudegladiator/YoutubeDownloader/issues"
    
})                       
st.cache()
st.title("Download any YouTube videos with best quality 🥳")

URL = st.text_input("Paste any YouTube URL/Link",placeholder="Enter Name/URL")
option = st.radio("Select Type: ", ('YouTube', 'URL Upload'))
if(st.button('Apply')):
     with st.spinner('Downloading...'):
         if (option == 'YouTube'):
            ydl_opts = {"outtmpl": "%(title)s.mp4"}
            results = YoutubeSearch(URL, max_results=1).to_dict()
            link=f"https://youtube.com{results[0]['url_suffix']}"
            title = results[0]["title"]
            yt = YouTube(link)
            with YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(link, download=False)
                video = ydl.prepare_filename(info)
                ydl.process_info(info)
                p = Path(video)
                p=p.rename(p.with_name(f"{title}"))
                with open(p,'rb') as f:
                st.write(f"{title}")
                st.video(f)
                st.download_button("Download Video 📥",data=f,file_name=f"{title}.mp4")
         else:
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
