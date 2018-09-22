#!/usr/local/bin/env python
import requests
import re
import base64


username = "natas11"
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'

url = 'http://%s.natas.labs.overthewire.org/' % username

cookieContent = 'ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK'

jar = requests.cookies.RequestsCookieJar()
jar.set('data', cookieContent, domain='natas11.natas.labs.overthewire.org', path='/')


response = requests.post(url, auth=(username, password), cookies=jar)
content = response.text


# print(content)
print(re.findall('natas12 is (.*)<br>', content)[0])
