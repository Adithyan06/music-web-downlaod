import os
import requests
import streamlit as st
from pathlib import Path
from pytube import YouTube
from yt_dlp import YoutubeDL
from streamlit_lottie import st_lottie
from youtube_search import YoutubeSearch

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_ej2lfhv2.json")

st.cache()
st.set_page_config(
    page_title="Download Any songs now !!",
    page_icon="♥️",
    menu_items={"Get help": "https://github.com/Adithyan06"})

st.title("YouTube Videos Downloader") 
st.caption("Download any Video/Audio Songs.Just copy the name or YouTube link of the song you want 🥳")
st_lottie(lottie_coding, height=280, key="YouTube")

query = st.text_input("Song Name or YouTube URL",placeholder="YouTube URL")
st.title("hey currently video and audio function is not working properly so please use urlupload option 🙏")
option = st.radio("Select Type: ", ('Video 🎥', 'Audio 🎶', 'URlUplaod 💦'))
if(st.button('Submit')):
     with st.spinner('Wait for it...'):
         try:
             if (option == 'Video 🎥'):
                res = st.selectbox("Select The resolution",("720p","360p","144p")) 
                results = YoutubeSearch(query, max_results=1).to_dict()
                yt = YouTube(f"https://youtube.com{results[0]['url_suffix']}")    
                title = results[0]["title"]                  
                video = yt.streams.get_by_itag(yt.streams.filter(res=res , progressive="True" )[0].itag)      
                hi = video.download()           
                p = Path(hi)
                p=p.rename(p.with_name(f"{title[:35]}.mp4"))      
                with open(p,'rb' ) as f:                
                    st.write(f"{title}")
                    st.video(f)
                    st.write("Link -", f"https://youtube.com{results[0]['url_suffix']}")
                    st.download_button("Save Video", data=f, file_name=f"{title[:35]}.mp4") 
             if (option == 'Audio 🎶'):   
                 url = "https://t-one-youtube-converter.p.rapidapi.com/api/v1/createProcess"
                 results = YoutubeSearch(query, max_results=1).to_dict()
                 link = f"https://youtube.com{results[0]['url_suffix']}"
                 querystring = {"url":link,"format":"mp3"} 
                 headers = {
 	                "X-RapidAPI-Key": "33af2319cbmshd1a3ee767f631f3p16a1dfjsnd5800101f122",
 	                "X-RapidAPI-Host": "t-one-youtube-converter.p.rapidapi.com"}
                 response = requests.get(url, headers=headers, params=querystring).json()
                 song = response.get('file')
                 st.audio(song)
             else:               
                 with YoutubeDL() as ydl:
                     info = ydl.extract_info(query, download=False)
                     video = ydl.prepare_filename(info)
                     ydl.process_info(info)
                     x = Path(video)
                     x=x.rename(x.with_name(f"{video}.mp4"))
                     with open(x,'rb') as xx:
                         st.write(video)
                         st.video(xx)
                         st.download_button("Download 🥀",data=xx,file_name=f"{video}.mp4")
         except Exception as e:
             st.write(e)
st.write(f"✨ You can find me in instagram as [Kannan 🌀](https://instagram.com/_ka.n.n.an._?igshid=MzNlNGNkZWQ4Mg==)")
