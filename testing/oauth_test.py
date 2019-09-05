import requests_oauthlib, requests

url = \ "https://api.twitter.com/1.1/account/verify_credentials.json"

oauth = requests_oauthlib.OAuth1(
    "<API_KEY>", 
    "<API_SECRET>",
    "<ACCESS_TOKEN>",
    "<ACCESS_TOKEN_SECRET>"
)

response = requests.get(url, auth=oauth)

print(response.json())


