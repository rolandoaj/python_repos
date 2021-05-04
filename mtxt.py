#! /usr/bin/python
f = open ('Holamundo.txt','wb')
f.write('hola mundo')
f.write("\n")
f.write('estoy programando en python')
f.close()

fse = open("Holamundo.txt","r")
print(fse.read())
fse.close()
