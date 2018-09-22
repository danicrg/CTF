#!/usr/local/bin/python3

from pwn import *

host = 'mngmnt-iface.ctfcompetition.com'
port = 1337

s = remote(host, port)

print(s.recv())

# binary in /proc/self
