#!/usr/local/bin/python3
import requests

url = "https://static.icec.tf/toke/"

response = requests.get(url)
content = response.text

print(content)
