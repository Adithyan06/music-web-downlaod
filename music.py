import streamlit as st
import requests
import wget
from pathlib import Path

def search_wallpapers(query, max_results=10):
    url = f"https://api.unsplash.com/search/photos"
    params = {
        "query": query,
        "client_id": "dKRzg3P20iERjrsD0_rIOhSYpVAYLTWtlYXhKDA5T-Y",
        "per_page": max_results,
        "orientation": "landscape",  # Forces landscape-oriented wallpapers
        "content_filter": "high",  # Filters for high-quality wallpapers
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["results"]

def display_wallpapers(wallpapers, max_results=10):
    count = 0
    for wallpaper in wallpapers:
        if count >= max_results:
            break
        st.image(wallpaper["urls"]["regular"], caption=wallpaper["alt_description"])
#       st.write(f"Download: [Link]({wallpaper['links']['download']})")
        st.download_button("Save Image", data=f"({wallpaper['urls']['regular']})", file_name="image.jpg") 
        count += 1

def main():

    st.title("Wallpaper Search")

    query = st.text_input("Enter a keyword to search wallpapers")
    option = st.radio("Select Type: ", ('Unsplash', 'Wallpaper'))
    if(st.button('Search')):
       with st.spinner('Downloading...'):
           if (option == 'Unsplash'):
             wallpapers = search_wallpapers(query)
             display_wallpapers(wallpapers)
           else:
               url = f"http://api.safone.me/wall?query={query}&limit=3"
               wall = requests.get(url=url).json()
               wallpaper = wall['results'][0]['imageUrl']
               title = wall['results'][0]['title']
#              y = Path(file)
#              y=y.rename(y.with_name(f"{title[:4]}.jpg"))
#              with open(y,'rb') as yy:                  
               st.image(wallpaper)  
               st.download_button("Save Image", data=wallpaper, file_name=f"{title[:4]}.jpg")
            
if __name__ == "__main__":
    main()
