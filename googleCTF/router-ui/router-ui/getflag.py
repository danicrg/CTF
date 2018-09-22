#!/usr/local/bin/python3

import requests

url = 'https://router-ui.web.ctfcompetition.com/'

s = requests.session()

response = s.get(url)

print(response.text)

username = 'flag'
password = 'flag'

response = s.post(url, params={'username':username, 'password':password})

print(response.text)