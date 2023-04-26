import streamlit as st
from pathlib import Path
from yt_dlp import YoutubeDL
from pytube import YouTube
from youtube_search import YoutubeSearch

st.set_page_config(page_title="Download Now",page_icon="🧡",menu_items={
    "Get help": "https://github.com/dudegladiator/YoutubeDownloader",
    "Report a bug" : "https://github.com/dudegladiator/YoutubeDownloader/issues"
    
})                       
st.cache()
st.title("Download any YouTube videos with best quality 🥳")
URL = st.text_input("Paste any YouTube URL/Link")
results = []
count = 0
while len(results) == 0 and count < 6:
    if count>0:
        time.sleep(1)
    results = YoutubeSearch(URL, max_results=1).to_dict()
    count += 1
    try:
       link = f"https://youtube.com{results[0]['url_suffix']}"
       title = results[0]["title"]
       yt = YouTube(link)
       if(st.button('Apply')):
            z = st.info("Please Wait...")
#           ydl_opts = {"outtmpl": f"{yt.title}.mp4"}
            with YoutubeDL() as ydl:
                info = ydl.extract_info(link, download=False)
                video = ydl.prepare_filename(info)
                ydl.process_info(info)
                p = Path(video)
                p=p.rename(p.with_name(f"{title[:33]}.mp4"))
                with open(p,'rb') as f:
                    st.write(f"{title}")
                    st.video(f)
                    st.download_button("Download Video 📥",data=f,file_name=f"{title}.mp4") 
