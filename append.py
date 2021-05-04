#! /usr/bin/python
import os
import sys
import fileinput

tbanner=["                                WARNING", "        Authorized Use Only and the use of this system is restricted to", "         authorized persons only. All others will be prosecuted to the", "                        full extent of the law."]
#pkernel=[]

#def append_last(fedit,nparameter):
#	with open(fedit, "a+") as mani_file:
#		mani_file.seek(0)
#		data = mani_file.read(100)
#		if len(data) > 0:
#			mani_file.write("\n")
#		mani_file.write(nparameter)

#for j in pkernel:
#	append_last("sysctl.conf",j)

banner = open("/home/anjimenez/scripts_python/banner.txt", "w")
for i in tbanner:
	banner.write(i + os.linesep)
banner.close()
