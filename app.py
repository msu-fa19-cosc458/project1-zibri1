import flask
import os
import json
import random 
import requests_oauthlib, requests

app = flask.Flask(__name__)


genius_url = "https://api.genius.com/search?q=Ari%20Lennox"
twitter_url = "https://api.twitter.com/1.1/search/tweets.json?q=%3AAriLennox"

oauth = requests_oauthlib.OAuth1(
    "5t5u4OYI4lmQ3ZUOHQp9tVFOV",
    "dP6Pxia2MlZYyhfx5X8uDv4QDmwbmelz7Gk8RpOyXcGKusVmZB",
    "506741435-8v0yQmfNyvCEr5IJFsbLQk7fRhnBSEBAVhF0HlD3",
    "8TlkYXLcutndQ5wrS51HNAoNhJmTc5nJfLiAbImVbwWCt")
    

my_headers = {
        "Authorization": "Bearer qiICws1IclXFRZmTwrTJI7k4m8vWoOwy2smTaAmQ2RuyiWztfrPPijT9ea2i2nA-"
}
    

genius_response = requests.get(genius_url, headers=my_headers)
genius_json_body = genius_response.json()
twitter_response = requests.get(twitter_url, auth=oauth)
twitter_json_body = twitter_response.json()

#print(twitter_response.json())
#print(twitter_json_body)
print(json.dumps(twitter_json_body, indent=2))

@app.route('/') 
def index(): 
  
    r = random.randint(0,9)
    z = random.randint(0,14)
    q = random.randint(0,14)
    v = random.randint(0,14)
    json_song = genius_json_body["response"]["hits"][r]["result"]["title"]
    ac = genius_json_body["response"]["hits"][r]["result"]["song_art_image_url"]
    ap = genius_json_body["response"]["hits"][r]["result"]["primary_artist"]["image_url"]
    tweet01 = twitter_json_body["statuses"][z]["text"]
    tweet02 = twitter_json_body["statuses"][q]["text"]
    tweet03 = twitter_json_body["statuses"][v]["text"]

    
    return flask.render_template("index.html", 
    song = json_song, album_cover = ac, artist_pic = ap, tweet1 = tweet01, tweet2 = tweet02, tweet3 = tweet03)
    

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)