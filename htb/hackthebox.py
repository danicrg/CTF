#!usr/local/bin/python3

import requests
import urllib3

url = 'http://hackthebox.eu/api/invite/generate'

response = requests.post(url)
content = response.text

print(response.content)

# RVVLUFQtUExaTVMtU0xEWVctWEZDUFAtUUlZWUY
