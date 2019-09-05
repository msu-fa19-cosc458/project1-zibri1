{"changed":true,"filter":false,"title":"app.py","tooltip":"/app.py","value":"import flask\nimport os\nimport requests\nimport json\nimport random \n\napp = flask.Flask(__name__)\n\n@app.route('/')  \ndef index(): \n    url = \"https://api.genius.com/search?q=Ari%20Lennox\"\n    \n    my_headers = {\n        \"Authorization\": \"Bearer qiICws1IclXFRZmTwrTJI7k4m8vWoOwy2smTaAmQ2RuyiWztfrPPijT9ea2i2nA-\"\n    }\n    \n    response = requests.get(url, headers=my_headers)\n    r = random.randint(0,9)\n    print(response.text)\n    json_body = response.json()\n    json_song = json_body[\"response\"][\"hits\"][r][\"result\"][\"title\"]\n    album_cover = json_body[\"response\"][\"hits\"][r][\"result\"][\"song_art_image_url\"]\n    artist_pic = json_body[\"response\"][\"hits\"][r][\"result\"][\"primary_artist\"][\"image_url\"]\n    print(album_cover)\n    print(json.dumps(json_body, indent = 2))\n    return flask.render_template(\"index.html\", song = json_song, i = album_cover, a = artist_pic)\n\napp.run(\n    port=int(os.getenv('PORT', 8080)),\n    host=os.getenv('IP', '0.0.0.0'),\n    debug=True\n)","undoManager":{"mark":0,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":31,"column":1},"action":"insert","lines":["import flask","import os","import requests","import json","import random ","","app = flask.Flask(__name__)","","@app.route('/')  ","def index(): ","    url = \"https://api.genius.com/search?q=Ari%20Lennox\"","    ","    my_headers = {","        \"Authorization\": \"Bearer qiICws1IclXFRZmTwrTJI7k4m8vWoOwy2smTaAmQ2RuyiWztfrPPijT9ea2i2nA-\"","    }","    ","    response = requests.get(url, headers=my_headers)","    r = random.randint(0,9)","    print(response.text)","    json_body = response.json()","    json_song = json_body[\"response\"][\"hits\"][r][\"result\"][\"title\"]","    album_cover = json_body[\"response\"][\"hits\"][r][\"result\"][\"song_art_image_url\"]","    artist_pic = json_body[\"response\"][\"hits\"][r][\"result\"][\"primary_artist\"][\"image_url\"]","    print(album_cover)","    print(json.dumps(json_body, indent = 2))","    return flask.render_template(\"index.html\",song = json_song, i = album_cover, a = artist_pic)","","app.run(","    port=int(os.getenv('PORT', 8080)),","    host=os.getenv('IP', '0.0.0.0'),","    debug=True",")"],"id":1}],[{"start":{"row":25,"column":46},"end":{"row":25,"column":47},"action":"insert","lines":[" "],"id":2}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":31,"column":1},"end":{"row":31,"column":1},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1567718033480}