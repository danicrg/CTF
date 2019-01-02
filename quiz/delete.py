#!/usr/local/bin/python3
import requests
from string import *
import re
import threading
import logging

s = requests.Session()

username = 'fsociety'
password = 's3z7DIDF6fdETRI'

# login funcional!!

url = 'https://quiz2019.herokuapp.com/session/'
data = {'login': username, 'password': password, 'redir': '/', 'commit': 'Login'}
response = s.post(url, data=data)


def deleteQuiz(session, id):
    session.get('https://quiz2019.herokuapp.com/quizzes/%s?_method=DELETE' % id)
    print('Borrada la pregunta con id: %s' % id)


still_questions = True

while still_questions:
    url = 'https://quiz2019.herokuapp.com/users/106/quizzes'
    response = s.get(url)
    ids = re.findall('<a href="/quizzes/(.*)/play">', response.text)
    if len(ids) != 0:
        for id in ids:
            t = threading.Thread(target=deleteQuiz, args=(s, id))
            t.start()
    else:
        still_questions = False

print('done!')
