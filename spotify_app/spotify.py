import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

username = sys.argv[1]

# https://open.spotify.com/user/cosminmarin

#scope = 

# Erase cache and prompt for user permissions
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

#create Spotify objectß
spotipyObject = spotipy.Spotify(auth=token)

user = spotipyObject.current_user()

print(json.dumps(user, sort_keys=True, indent=4))

displayName = user['display_name']
