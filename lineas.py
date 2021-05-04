#! /usr/bin/python
import os
import sys
import fileinput

print ("+++ 1 ++++")
datos = []
with open("/home/anjimenez/scripts_python/ssh/sshd_config") as fname:
	lineas = fname.readlines()
	for linea in lineas:
		datos.append(linea.strip('\n'))
print (datos)
print ("+++")

print ("Find PermitRootLogin")
n="#PermitRootLogin yes"

if n in datos:
	print("Existe la cadena")
else:
	print("No esta la cadena")
