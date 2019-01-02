#!/bin/bash

cat m3ss@g#_f0r_pAuL |tr '[A-Za-z]' '[N-ZA-Mn-za-m]' > message;
fcrackzip -v -l 4 -u BAND.zip;
echo "pass" > pw;
unzip BAND.zip;
 
