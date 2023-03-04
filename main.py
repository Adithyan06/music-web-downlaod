import streamlit as st
from pathlib import Path
from pytube import YouTube
import os , time,random,sys
import time
import ffmpeg
from youtube_search import YoutubeSearch
from streamlit_lottie import st_lottie

st.cache()
st.set_page_config(page_title="Download Any songs now !!",page_icon="images/logo.png",menu_items={
    "Get help": "https://github.com/dudegladiator/YoutubeDownloader"    
})

lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/private_files/lf30_YcIv9u.json")
st.title("Download Youtube Audio")
image_column = st.columns((1))
with image_column:
        st_lottie(lottie_coding, height=300, key="music")
st.caption("Download any Video/Audio Songs.Just copy the name or YouTube link of the song you want 🥳")
query = st.text_input("Youtube Video or Playlist URL")
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
                res = st.selectbox("Select The resolution",("720p","360p","240p","144p"))
                if(st.button('Submit')):
                     st.info("Please Wait....")
                     video = yt.streams.get_by_itag(yt.streams.filter(res=res , progressive="True" )[0].itag)      
                     hi = video.download()           
                     p = Path(hi)
                     p=p.rename(p.with_name(f"{title}.mp4"))
                     with open(p,'rb' ) as f:                
                         st.write(f"{title}")
                         st.video(f)
                         st.download_button("Save Video", data=f, file_name=f"{title}.mp4") 
          else:
               if(st.button('Submit')):
                   st.info("Please Wait....")
                   audio = yt.streams.get_by_itag(yt.streams.filter(type="audio",mime_type="audio/webm")[0].itag)
                   a = audio.download()
                   ma = Path(a)
                   ma=ma.rename(ma.with_name(f"{title}.mp3"))   
                   with open(ma,'rb' ) as s:                
                       st.write(f"{title}")
                       st.audio(s)
                       st.download_button("Save Audio", data=s, file_name=f"{title}.mp3")      
      except Exception as e:
          st.info("Song not found")
          st.write(e)
except Exception:
    st.info("not found")
