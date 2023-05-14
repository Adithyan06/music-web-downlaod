import os

import streamlit as st

import spotdl

# Set up the Streamlit app

st.title("Spotify Song Downloader")

# Input field for the Spotify song URL

spotify_url = st.text_input("Enter the Spotify song URL")

# Download button

if st.button("Download"):

    if spotify_url:

        # Specify the download directory

        download_dir = "downloads"

        # Create the download directory if it doesn't exist

        if not os.path.exists(download_dir):

            os.makedirs(download_dir)

        # Change the current working directory to the download directory

        os.chdir(download_dir)

        # Download the song from Spotify

        try:

            spotdl.main([spotify_url])

            st.success("Download complete!")

        except Exception as e:

            st.error(f"An error occurred: {e}")

    else:

        st.warning("Please enter a Spotify song URL")

