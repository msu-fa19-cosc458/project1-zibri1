import flask
import random
import os

app = flask.Flask(__name__)

@app.route('/')
def index(): 
    return '<html itemscope="" itemtype="http://schema.org/WebPage" lang="en"><head><meta content="Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking for." name="description"><meta content="noodp" name="robots"><meta content="/logos/doodles/2017/bessie-colemans-125th-birthday-5751652702224384-hp.gif" itemprop="image"><link href="/images/branding/product/ico/googleg_lodp.ico" rel="shortcut icon"><meta content="Bessie Coleman’s 125th birthday! #GoogleDoodle" property="og:description">...'
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')