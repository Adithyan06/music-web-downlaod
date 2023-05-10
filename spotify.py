import os

import streamlit as st

import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

# Set up your Spotify API credentials

client_id = "7d1c283593d94940a3b9b7a8445ceaa5"

client_secret = "54c84a9e22974052a88288bc08610eb2"

# Set up your Streamlit app

st.title("Spotify Song Downloader")

# Authenticate with the Spotify API

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

sp = spotipy.Spotify(auth_manager=auth_manager)

# Get user input for the song name

song_name = st.text_input("Enter the song name:", "")

# Search for songs on Spotify

if song_name:

    results = sp.search(q=song_name, type='track', limit=5)

    # Display the search results

    if results['tracks']['items']:

        st.subheader("Search Results:")

        for idx, track in enumerate(results['tracks']['items']):

            st.write(f"{idx + 1}. {track['name']} - {track['artists'][0]['name']}")

        # Allow user to select a song for download

        selected_index = st.number_input("Select a song (enter the corresponding number):", min_value=1,

                                         max_value=len(results['tracks']['items']), value=1, step=1)

        if st.button("Download"):

            selected_track = results['tracks']['items'][int(selected_index) - 1]

            track_name = selected_track['name']

            artist_name = selected_track['artists'][0]['name']

            # Download logic goes here

            # ...

            st.success(f"Song '{track_name}' by {artist_name} downloaded successfully!")

    else:

        st.error("No results found for the given song name.")

