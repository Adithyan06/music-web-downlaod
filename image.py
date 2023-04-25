import streamlit as st
from pathlib import Path
from yt_dlp import YoutubeDL
from pytube import YouTube
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_bwk2zS.json")

st.set_page_config(page_title="Download Now",page_icon="🧡",menu_items={
    "Get help": "https://github.com/dudegladiator/YoutubeDownloader",
    "Report a bug" : "https://github.com/dudegladiator/YoutubeDownloader/issues"
    
})                       
st.cache()
column = st.columns(1)
with column:
        st_lottie(lottie_coding, height=300, key="coding")

st.title("Download any YouTube videos with best quality 🥳")
URL = st.text_input("Paste any YouTube URL/Link")
yt = YouTube(URL)
if(st.button('Apply')):
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
