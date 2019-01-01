#!usr/local/bin/python3

import requests

url = "http://10.10.10.105"

response = requests.post(url, data={'username': '../..', 'password': '..'})

print(response.text)
