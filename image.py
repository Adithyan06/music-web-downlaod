import os , time,random,sys
import wget
import time
import streamlit as st
import requests
from pathlib import Path
from yt_dlp import YoutubeDL
from pytube import YouTube


API = "https://apis.xditya.me/lyrics?song="

def search(query):
        r = requests.get(API + query)
        find = r.json()
        return find
       
def lyrics(query):
        fin = search(query)
        text = f'**🎶 Successfully Extracted Lyrics Of {query} 🎶**\n\n\n\n'
        text += f'{fin["lyrics"]}'
        return text

st.set_page_config(page_title="Download Now",page_icon="kannan/logo.png",menu_items={
    "Get help": "https://github.com/dudegladiator/YoutubeDownloader",
    "Report a bug" : "https://github.com/dudegladiator/YoutubeDownloader/issues"
    
})                       

st.cache()
st.title("Download Cover Images of any Song 🥳")
URL = st.text_input("Link")
yt = YouTube(URL)
if(st.button('submit')):
     ydl_opts = {"outtmpl": f"{yt.title}.mp4"}
     with YoutubeDL() as ydl:
         info = ydl.extract_info(URL, download=False)
         video = ydl.prepare_filename(info)
         ydl.process_info(info)
         p = Path(video)
         p=p.rename(p.with_name(f"{yt.title[:33]}.mp4"))
         with open(p,'rb') as f:
             st.video(f)
             st.download_button("Download Video 📥",data=f)  

# hello = st.text_input("Enter your query")
# if(st.button('Submit')):
#    link = f"http://api.safone.me/image?query={hello}&limit=2"
#    dato = requests.get(url=link).json()
#    pr = dato['results'][0]['imageUrl']
#    title = dato['results'][0]['title']
#    image = wget.download(pr)
#    st.write(title)
#    st.image(image)
#    st.download_button("Download Image",data=image)
