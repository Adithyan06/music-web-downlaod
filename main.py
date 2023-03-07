import streamlit as st
from pathlib import Path
from pytube import YouTube
from yt_dlp import YoutubeDL
import os
import time
import ffmpeg
from youtube_search import YoutubeSearch
import requests
import wget

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
          time.sleep(0.3)
        results = YoutubeSearch(query, max_results=1).to_dict()
        count += 1
    try:
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"]
        yt = YouTube(link)

        if (option == 'Video 🎥'):
           res = st.selectbox("Select The resolution",("720p","360p","144p"))                
           video = yt.streams.get_by_itag(yt.streams.filter(res=res , progressive="True" )[0].itag)      
           hi = video.download()           
           p = Path(hi)
           p=p.rename(p.with_name(f"{yt.title[:35]}.mp4"))
           if(st.button('Submit')):
                st.info("Please Wait....")
                with open(p,'rb' ) as f:                
                    st.write(f"{yt.title}")
                    st.video(f)
                    st.download_button("Save Video", data=f, file_name=f"{title[:35]}.mp4") 
        else:
             musics = st.radio("Where should I download music from?", ('Youtube', 'JioSaavn'))
             if (musics == 'JioSaavn'):
                try:
                    r = requests.get(f"https://saavn.me/search/songs?query={query}&page=1&limit=1").json()    
                    sname = r['data']['results'][0]['name']
                    slink = r['data']['results'][0]['downloadUrl'][4]['link']
                    img = r['data']['results'][0]['image'][2]['link']
                    thumbnail = wget.download(img)
                    file = wget.download(slink)
                    ffile = file.replace("mp4", "mp3")
                    os.rename(file, ffile)
                    if(st.button('Submit')):
                         st.image(thumbnail)  
                         st.audio(ffile)
                         st.download_button("Save Audio", data=ffile, file_name=f"{sname}.mp3") 
                except Exception as e:
                    st.write(" Something wrong 😕")    
                    print(e) 
             else:                 
                  audio = yt.streams.get_by_itag(yt.streams.filter(type="audio",mime_type="audio/webm")[0].itag) 
                  a = audio.download()
                  ma = Path(a)
                  ma=ma.rename(ma.with_name(f"{title[:33]}.mp3"))  
                  if(st.button('Submit')): 
                       st.info("Please Wait....")
                       with open(ma,'rb' ) as s:                
                           st.write(f"{title[:33]}")
                           st.audio(s)
                           st.download_button("Save Audio", data=s, file_name=f"{yt.title[:33]}.mp3")  
except Exception as e:
    st.write("Something went Wrong")    
    print(e) 
