#! /usr/bin/python
import os
import sys
import fileinput
import re, mmap
import shutil
import subprocess
from os import remove

def insertafter(archive,numberline,newline):
	names = []
	with open(archive, 'r+') as fd:
    		for line in fd:
			names.append(line.splitlines()[-1].strip())

    		names.insert(numberline,newline)
    		fd.seek(0)
    		fd.truncate()

    		for i in xrange(len(names)):
        		fd.write("%s\n" %(names[i]))

insertafter("password-auth",8,"auth        required      pam_tally2.so deny=5 unlock_time=600 file=/var        /log/faillog quiet")
