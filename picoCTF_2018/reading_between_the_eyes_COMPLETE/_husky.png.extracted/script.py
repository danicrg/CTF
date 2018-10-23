#!/usr/local/bin/python3

import glob
import zlib
import sys

compressed = open('29.zlib', 'rb')

# with open(filename + '-decompressed', 'wb') as expanded:
data = zlib.decompress(compressed.read())
# expanded.write(data)
print(data)
