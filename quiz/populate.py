#!/usr/local/bin/python3
import requests
from string import *
import re
import threading


# Numero de preguntas
repeat = 10


s = requests.Session()

message = 'With great power comes great responsability'

username = 'fsociety'
password = 's3z7DIDF6fdETRI'

# login funcional!!

url = 'https://quiz2019.herokuapp.com/session/'
data = {'login': username, 'password': password, 'redir': '/', 'commit': 'Login'}
response = s.post(url, data=data)


def crearQuiz(session, data, files, number):
    session.post(url, data=data, files=files)
    print('Question %i created' % number)


url = 'https://quiz2019.herokuapp.com/quizzes/'
data = {'question': message, 'answer': 'Error'}
files = {'image': ('fotillo', open('i.gif', 'rb'), {'Expires': '0'})}
for i in range(0, repeat):
    t = threading.Thread(target=crearQuiz, args=(s, data, files, i))
    t.start()
