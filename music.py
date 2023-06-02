import streamlit as st

import requests

def search_wallpapers(query):

    url = f"https://api.unsplash.com/search/photos?query={query}&client_id=dKRzg3P20iERjrsD0_rIOhSYpVAYLTWtlYXhKDA5T-Y"

    response = requests.get(url)

    data = response.json()

    return data["results"]

def display_wallpapers(wallpapers):

    for wallpaper in wallpapers:

        st.image(wallpaper["urls"]["regular"], caption=wallpaper["alt_description"])

def main():

    st.title("Wallpaper Search")

    query = st.text_input("Enter a keyword to search wallpapers")

    if st.button("Search"):

        wallpapers = search_wallpapers(query)

        display_wallpapers(wallpapers)

if __name__ == "__main__":

    main()
