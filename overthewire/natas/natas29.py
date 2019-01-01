#!/usr/local/bin/python3
import requests
import re

username = "natas29"
password = "airooCaiseiyee8he8xongien9euhe8b"

url = 'http://%s.natas.labs.overthewire.org/' % username

s = requests.session()

file = 'perl underground 2'

response = s.get(url + 'index.pl?file=' + file, auth=(username, password))

print(response.text)
