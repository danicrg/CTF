# WEB
- Check for robots.txt
- gobuster -u (url) http://... -w [wordlist]
- searchsploit -r (buscar exploits de apps web)
- sqlmap:

		sqlmap -u URL --method=POST --data="user=&password=" -p "user" --dbs
- wpscan: scanner for wordpress
	- --url
	- --enumerate [-u for usernames]
	- --log

# BINARY EXPLOITATION
- to get asm code run 'objdump -d [binary file] > out.S'
- gdb

# STEGO
- strings
- xxd or hexdump -C
- binwalk
- steghide extract -sf
- fcrackzip

		fcrackzip -v -m zip6 -l 4-8 -u secret.zip
		fcrackzip -v -D -u -p /usr/share/dict/words secret.zip
- password generator: https://github.com/Broham/PassGen

# SHELL
- vim:
	- :colo elflord
- vulnerabilities in commands: gtfobins.github.io
- tmux:
	^B +
	- , (rename window)
	- ! (new window from split)
	- & (kill window)
	- % (vertical split)
	- " (horizontal split)
	- arrows (switch windows)

# BOXES
- sudo -l: gives the files you can access without root password
- reverseshells: https://github.com/infodox/python-pty-shells

## nmap:
- sT -> three way handshake
- sC -> standard scripts
- sV -> versions
- oA

## METASPLOIT
to start it:
		
		service postgresql start
		msfdb init
		msfconsole

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
	- options
	- payloads
	- targets
	- info: about the exploit
- set: set options
- search:
	- platform:[windows, linux..]
	- name
	- type:[type of module]
- exploit: runs the exploit
- back: unload a module
- exit: exit metasploit

Modules are stored in /usr/share/metasploit-framework/modules

