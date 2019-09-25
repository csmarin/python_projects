import os
import sys
import json, spotipy, webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

username = sys.argv(1)

# https://open.spotify.com/user/cosminmarin

# Erase cache and prompt for user permissions
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache=(username)")
    token = util. prompt_for_user_token(username)

#create Spotify object
spotipyObject = spotipy.Spotify(auth=token)

