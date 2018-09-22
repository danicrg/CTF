#!/usr/local/bin/python3
import requests
import re
import codecs

username = "natas27"
password = "55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ"

url = 'http://%s.natas.labs.overthewire.org/' % username

s = requests.session()

response = s.get(url, auth=(username, password))

print(response.text)
