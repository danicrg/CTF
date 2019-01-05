#!/usr/bin/python3

from subprocess import call
from subprocess import check_output
import re

name = check_output('ls', shell=True)
name = re.findall('(.*).zip', str(name))[0] 
name = (name + '.zip').replace("b'", "")

while True:
    password = check_output('binwalk %s' % name, shell=True)
    if ".zip" in str(password):
        password = re.findall('name: (.*).zip', str(password))[0]
        print('password: ' + password)
        call('unzip -P %s %s' % (password, name), shell=True)
        call('rm %s' % name, shell=True)
        name = password + '.zip'
    else:
        break

call('unzip -P letmeinplease *.zip', shell=True)
flag = check_output('strings DoNotTouch | grep HTB', shell=True)
flag = re.findall('HTB{(.*)}', str(flag))[0]
print('HTB{' + flag+ '}')
