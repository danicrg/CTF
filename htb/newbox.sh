#!/bin/bash

openvpn danicrg.ovpn &;
mkdir boxes/$1;
cd boxes/$1;
nmap -sV -sC -oA nmap $2
