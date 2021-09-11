import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import urllib.parse
import json


url = 'https://linkareer.com/cover-letter/search?page=1&tab=all'
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
print(response.getcode())

response_body = response.read()
response_body_dict = str(response_body.decode('utf-8')).strip("'<>() ").replace('\'', '\"')
