# WEB
Check for robots.txt
gobuster -u (url) http://... -w [wordlist]
searchsploit -r (buscar exploits de apps web)

- sqlmap:
 sqlmap -u URL --method=POST --data="user=&password=" -p "user" --dbs

# BINARY EXPLOITATION
to get asm code run 'objdump -d [binary file] > out.S'
GDB

# STEGO
- steghide extract -sf

# SHELL
vim:
- :colo elflord
vulnerabilities:
in commands
gtfobins.github.io
tmux:
^B +
- % (vertical split)
- " (horizontal split)
- arrows (switch windows)

# BOXES
nmap:
- sT -> three way handshake (whatever that means)
- sC
- sV
- oA
wpscan: scanner for wordpress
- --url
- --enumerate [-u for usernames]
- --log
sudo -l: gives the files you can access without root password
reverseshells:
https://github.com/infodox/python-pty-shells
## METASPLOIT
to start it:
- service postgresql start
- msfdb init
- msfconsole
6 types of modules:
- exploits: take advantage of a systems vulnerability and install a payload on the system.
- payloads: what we will try and plant on the system. Usually called rootkits.
	- singles: small pieces of code designed to take one single action.
	- stagers: to perform or create a communication between target and attacker.
	- stages: large payloads allowing potentially bigger atacks.
- auxiliary: unique types of attacks, robust tools. DOS functionality, scanners, crawlers, sniffers...
- encoders: to re-encode payloads. To get past security systems (anti-virus). Evasion techniques.
- nops: no-operation. Forces a processor to do nothing for an entire clockcycle. To exploit the buffer overflow
- post: after the system has been exploited.
useful commands:
- help
- use: allow to load a module.
- show: give you information on the module yo have loaded.
	options
	payloads
	targets
	info: about the exploit
- set: set options
- search:
	platform:[windows, linux..]
	name
	type:[type of module]
- exploit: runs the exploit
- back: unload a module
- exit: exit metasploit
Modules are stored in /usr/share/metasploit-framework/modules
