import streamlit as st
import wget
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials
#import wget
import urllib.request
import os

# Set up Spotify API credentials

client_id = '7d1c283593d94940a3b9b7a8445ceaa5'

client_secret = '54c84a9e22974052a88288bc08610eb2'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Streamlit app

st.title("Spotify Song Downloader")

# Input field for searching a song

song_name = st.text_input("Enter the song name:", value='', key='song_name')

# Button for searching and downloading the song

if st.button("Download"):

    if song_name:

        try:

            # Search for the song on Spotify

            results = sp.search(q=song_name, type='track', limit=1)

            if results and results['tracks']['items']:

                track = results['tracks']['items'][0]

                track_name = track['name']

                artist_name = track['artists'][0]['name']

                preview_url = track['preview_url']

                # Download the song

                if preview_url:

                    st.info(f"Downloading '{track_name}' by {artist_name}...")

                    file_name = f"{artist_name}_{track_name}.mp3"
                    song_file = f"{song_name}.mp3"
                    urllib.request.urlretrieve(preview_url, file_name)
                    os.system(f"wget -O '{song_file}' '{preview_url}'")
                    st.audio(song_file)
                    st.success(f"Song downloaded successfully. File name: {file_name}")

                else:

                    st.error("Sorry, the song preview is not available for download.")

            else:

                st.error("No results found for the given song name.")

        except Exception as e:

            st.error(f"An error occurred: {str(e)}")

    else:

        st.warning("Please enter a song name.")


                
