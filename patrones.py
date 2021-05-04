#! /usr/bin/python
import os
import sys
import fileinput
import re, mmap

patron='^.PermitRootLogin'
a="/home/anjimenez/scripts_python/ssh/sshd_config"
nvalue='PermitRootLogin no'
def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

replaceAll(a,patron,nvalue)
