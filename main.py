import streamlit as st
from pathlib import Path
from pytube import YouTube
import os , time,random,sys
from youtube_search import YoutubeSearch

def shorten_audio_option(opt):
    return opt.split("/")[-1]

st.cache()
def download (query,res):
    results = YoutubeSearch(query, max_results=1).to_dict()
    link = f"https://youtube.com{results[0]['url_suffix']}"
    title = results[0]["title"]
    yt = YouTube(link)
     
    audio = yt.streams.get_by_itag(yt.streams.filter(type="audio",mime_type="audio/webm")[0].itag)
    a = audio.download()
    global q
    q=Path(a)
    q=q.rename(q.with_name(f"{title}.mp3"))

st.set_page_config(page_title="Download Now",page_icon="images/logo.png",menu_items={
    "Get help": "https://github.com/dudegladiator/YoutubeDownloader",
    "Report a bug" : "https://github.com/dudegladiator/YoutubeDownloader/issues"
    
})
st.title("Download Youtube Video")
query=st.text_input("Youtube Video or Playlist URL")
a=st.button("Start Downloading 🙂")  
song = st.selectbox(
    "Pick an MP3 to play",
    (
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
        "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3",
    ),
    0,
    shorten_audio_option,
)

st.audio(song)
#    download(query, res="720p")
#    st.write(f"{title}")
#    with open(q,'rb' ) as f:
#        st.download_button("Save Audio",f,file_name=f"{title}.mp3")
