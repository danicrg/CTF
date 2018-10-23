#!/usr/local/bin/python3

cipher = 'd]Wc7H:oW5YgUFS7]D\9fGS^iGHSUF9bHSg9WIf9q'

shift = 12
plain = ''
for i in cipher:
    plain += chr(shift + ord(i))

print(plain)
