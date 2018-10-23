#!/bin/bash

/usr/local/Cellar/john-jumbo/1.8.0/share/john/unshadow ./passwd ./shadow > ./result.db
/usr/local/Cellar/john-jumbo/1.8.0/share/john/john ./result.db
