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
        text = f'**🎶 Successfully Extracted Lyrics Of {query} 🎶**\n\n\n\n'
        text += f'{fin["lyrics"]}'
        return text

st.set_page_config(page_title="Download Now",page_icon="kannan/logo.png",menu_items={
    "Get help": "https://github.com/dudegladiator/YoutubeDownloader",
    "Report a bug" : "https://github.com/dudegladiator/YoutubeDownloader/issues"
    
})                       

st.cache()
st.title("Download Cover Images of any Song 🥳")
hello = st.text_input("Enter your name")
color = st.text_input("Enter Your Colour")
if(st.button('Submit')):
     link = f"http://api.safone.me/image?query={hello}&limit={color}"
     dato = requests.get(url=link).json()
#    image = wget.download(thums)
     st.write(dato)
#    st.image(image)
#    st.download_button("Download Image",data=image)
