#!/usr/local/bin/env python
import requests
import re
import base64


username = "natas8"
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'

url = 'http://%s.natas.labs.overthewire.org/' % username

secret = 'oubWYf2kBq'

response = requests.post(url, auth=(username, password), data={"secret": secret, "submit": "submit"})
content = response.text
# print(content)
print(re.findall('Access granted. The password for natas9 is (.*)', content)[0])
