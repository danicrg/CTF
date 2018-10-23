#!/usr/local/bin/python3
import requests
import re


username = "natas28"
password = "JWwR438wkgTsNKBbcJoowyysdM82YjeF"

url = 'http://%s.natas.labs.overthewire.org/' % username

s = requests.session()

data = {'query': 'natas28'}

response = requests.post(url, auth=(username, password), data=data)
content = response.text

print(content)
