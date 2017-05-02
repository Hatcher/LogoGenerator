import requests
import urllib
import json
import os
from requests_oauthlib import OAuth1

with open ("login.txt", "r") as myfile:
    data = myfile.read().split()
    myfile.close()
print data
key1 = data[0]
key2 = data[1]

auth = OAuth1(key1, key2)
endpoint = "http://api.thenounproject.com/icon/1"

#Download and save an image at the url
def downloadImage(url):
    os.chdir('./')
    image = urllib.URLopener()
    image.retrieve(url, 'file.svg')

#Should download images based on specific tags, is it possible to determine if its an svg?

response = requests.get(endpoint, auth=auth)
data = json.loads(response.content)
imageUrl = data["icon"]["icon_url"]



downloadImage(imageUrl)
