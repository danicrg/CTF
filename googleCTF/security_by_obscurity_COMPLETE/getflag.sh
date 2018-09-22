#!/bin/bash

while [ `ls -rS | sed -n '2p'` != 'password' ]
do
	#unzip `ls -rS | sed -n '2p'`
	#mv data data.xz;
	#unxz data.xz;
	mv data data.gz;
	gunzip data.gz;
done

	
