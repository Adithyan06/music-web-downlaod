import streamlit as st

import requests

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

    if st.button("Search"):

        wallpapers = search_wallpapers(query)

        display_wallpapers(wallpapers)

if __name__ == "__main__":

    main()
