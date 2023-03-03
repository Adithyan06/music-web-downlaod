import os , time,random,sys
import wget
import time
import streamlit as st
import requests
from pathlib import Path


API = "https://apis.xditya.me/lyrics?song="

def search(query):
        r = requests.get(API + query)
        find = r.json()
        return find
       
def lyrics(query):
        fin = search(query)
        text = f'**🎶 Successfully Extracted Lyrics Of {song} 🎶**\n\n\n\n'
        text += f'`{fin["lyrics"]}`'
        return text

st.set_page_config(page_title="Download Now",page_icon="kannan/logo.png",menu_items={
    "Get help": "https://github.com/dudegladiator/YoutubeDownloader",
    "Report a bug" : "https://github.com/dudegladiator/YoutubeDownloader/issues"
    
})                       

st.cache()
st.title("Download Cover Images of any Song 🥳")
query = st.text_input("Enter a Song Name 🎶")
if(st.button('Submit')):
     result = query.title()
     st.success(result)
     link = f"https://api.deezer.com/search?q={query}&limit=1"
     dato = requests.get(url=link).json()
     try:
         match = dato.get("data")
         urlhp = match[0]
         thums = urlhp["album"]["cover_big"]
         thumb = wget.download(thums)
         st.image(thumb)
         rpl = lyrics(query)
         st.write(rpl)
     except Exception:
         st.write("Results Not Found")
