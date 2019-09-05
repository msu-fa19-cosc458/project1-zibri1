import requests

url = "https://api.genius.com/search?q=Ari%20Lennox"

my_headers = {
    "Authorization": "Bearer qiICws1IclXFRZmTwrTJI7k4m8vWoOwy2smTaAmQ2RuyiWztfrPPijT9ea2i2nA-"
}

response = requests.get(url, headers=my_headers)
print(response.text)
json_body = response.json()
print(json_body["response"]["hits"][0]["type"])