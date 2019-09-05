import flask
import os
import requests
import json
import random 

app = flask.Flask(__name__)

@app.route('/')  
def index(): 
    url = "https://api.genius.com/search?q=Ari%20Lennox"
    
    my_headers = {
        "Authorization": "Bearer qiICws1IclXFRZmTwrTJI7k4m8vWoOwy2smTaAmQ2RuyiWztfrPPijT9ea2i2nA-"
    }
    
    response = requests.get(url, headers=my_headers)
    r = random.randint(0,9)
    print(response.text)
    json_body = response.json()
    json_song = json_body["response"]["hits"][r]["result"]["title"]
    album_cover = json_body["response"]["hits"][r]["result"]["song_art_image_url"]
    artist_pic = json_body["response"]["hits"][r]["result"]["primary_artist"]["image_url"]
    print(album_cover)
    print(json.dumps(json_body, indent = 2))
    return flask.render_template("index.html",song = json_song, i = album_cover, a = artist_pic)

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)