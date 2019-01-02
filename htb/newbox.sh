#!/bin/bash

openvpn danicrg.ovpn &
mkdir boxes/$1;
cd boxes/$1;
sleep(4000);
nmap -sV -sC -oA nmap/$1 $2 &
