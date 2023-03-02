import os , time,random,sys
import time
import streamlit as st
import requests
from pathlib import Path

st.set_page_config(page_title="Download Now",page_icon="images/logo.png",menu_items={
    "Get help": "https://github.com/dudegladiator/YoutubeDownloader",
    "Report a bug" : "https://github.com/dudegladiator/YoutubeDownloader/issues"
    
})                       

st.cache()
st.title("Download Youtube Video")
query = st.text_input("Youtube Video or Playlist URL")
if(st.button('Submit')):
     result = query.title()
     st.success(result)
     link = f"https://api.deezer.com/search?q={query}&limit=1"
     dato = requests.get(url=link).json()
     thums = urlhp["album"]["cover_big"]
     thumb = wget.download(thums)
     st.image(thumb)
