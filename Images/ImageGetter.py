import requests
import urllib
import json
import os
from requests_oauthlib import OAuth1

auth = OAuth1("7af419d2f32240239aa335e5b0795ae2", "178fb1a58c2645d1af9aed853b23ad0a")
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
