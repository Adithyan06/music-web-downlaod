import streamlit as st
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

# Spotify API credentials
CLIENT_ID = "b1dcbb0c6d0f452f9f01710440ffce9c"
CLIENT_SECRET = "2b01cc24bb674e87a18d773e671c8660"

# Setting up the Spotify API client
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Streamlit app
st.title("Spotify Song Search")

# Input box to search for songs
search_query = st.text_input("Enter a song name or artist:")

# Button to perform the search
if st.button("Search"):
    if search_query:
        # Search for tracks
        results = sp.search(q=search_query, type='track', limit=10)
        tracks = results['tracks']['items']

        # Display the results
        for idx, track in enumerate(tracks):
            st.subheader(f"Result {idx + 1}")
            st.write(f"**Track Name:** {track['name']}")
            st.write(f"**Artist:** {track['artists'][0]['name']}")
            st.write(f"**Album:** {track['album']['name']}")
            st.image(track['album']['images'][0]['url'], width=300)
            st.write(f"[Open on Spotify]({track['external_urls']['spotify']})")
    else:
        st.write("Please enter a search term.")

st.write("Anas is killadi")
x = st.text_input("Enter a number:")
