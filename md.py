#! /usr/bin/python
import os
import sys
import fileinput
import re, mmap

#REGEX = 'PermitRootLogin'

with open('/home/anjimenez/scripts_python/ssh/sshd_config', 'r') as f:
	x= re.search(r"\bP\w+",f)
	print(x.string)
#	for line in f:
#        	if re.search(REGEX,f):  
#			print re.search(REGEX,f)

#with open('/home/anjimenez/scripts_python/ssh/sshd_config', 'r+') as f:
#  data = mmap.mmap(f.fileno(), 0)
#  mo = re.search(r'PermitRootLogin_(\d+)', data)
#  if mo:
#    print "found error", mo.group(1)

#def replaceAll(fil,searchExp,replaceExp):
#	for line in fileinput.input(fil, inplace=1):
#		if searchExp in line:
#			line = line.replace(searchExp,replaceExp)
#		sys.stdout.write(line)

#replaceAll('/home/anjimenez/scripts_python/ssh/sshd_config','^PermitRootLogin yes$','PermitRootLogin no')
