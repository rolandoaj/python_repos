#! /usr/bin/python
import os
import sys
import fileinput
import re, mmap
import shutil
import subprocess
from os import remove

a="/home/anjimenez/scripts_python/ssh/sshd_config"
logindef="/etc/login.defs"
dssh="/home/anjimenez/scripts_python/ssh/bckp"
respssh="/home/anjimenez/scripts_python/ssh/bckp/sshd_configbckp"

befssh= ['#PermitRootLogin yes', '#LogLevel INFO', '#IgnoreRhosts yes', '#HostbasedAuthentication no', '#PermitEmptyPasswords no', '#PermitUserEnvironment no', '#ClientAliveInterval 0', '#ClientAliveCountMax 3', '#Banner none', '#MaxAuthTries 6', 'X11Forwarding yes', '#UseDNS']
aftssh= ['PermitRootLogin no', 'LogLevel INFO', 'IgnoreRhosts yes', 'HostbasedAuthentication no', 'PermitEmptyPasswords no', 'PermitUserEnvironment no', 'ClientAliveInterval 900', 'ClientAliveCountMax 0', 'Banner /etc/ssh/sshd-banner', 'MaxAuthTries 5', 'X11Forwarding no', 'UseDNS no']
pkernel=['net.ipv4.ip_forward = 1', 'net.ipv4.conf.all.send_redirects = 0', 'net.ipv4.conf.default.send_redirects = 0', 'net.ipv4.conf.default.accept_source_route = 0', 'net.ipv4.conf.all.accept_redirects = 0', 'net.ipv4.conf.all.secure_redirects = 0', 'net.ipv4.conf.all.log_martians = 1', 'net.ipv4.conf.default.log_martians = 1', 'net.ipv4.icmp_echo_ignore_broadcasts = 1', 'icmp_ignore_bogus_error_responses = 1', 'all.rp_filter = 1', 'net.ipv4.conf.default.rp_filter = 1', 'net.ipv4.tcp_syncookies = 1', 'net.ipv6.conf.all.disable_ipv6 = 1', 'net.ipv6.conf.default.disable_ipv6 = 1']
tbanner=["                                WARNING", "        Authorized Use Only and the use of this system is restricted to", "         authorized persons only. All others will be prosecuted to the", "                        full extent of the law."]
aldef=['PASS_MAX_DAYS   99999', 'PASS_MIN_DAYS   0', 'PASS_MIN_LEN    5', 'PASS_WARN_AGE   7']
bldef=['PASS_MAX_DAYS   90', 'PASS_MIN_DAYS    7', 'PASS_MIN_LEN    8', 'PASS_WARN_AGE   14']
def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

def backpfile(dbck,source,desbck):
	os.mkdir(dbck)
	shutil.copy(source,desbck)

def append_last(fedit,nparameter):
        with open(fedit, "a+") as mani_file:
                mani_file.seek(0)
                data = mani_file.read(100)
                if len(data) > 0:
                        mani_file.write("\n")
                mani_file.write(nparameter)

##Enhance ssh
backpfile(dssh,a,respssh)
for n in range(len(bef)):
	replaceAll(a,befssh[n],aftssh[n])
append_last("/home/anjimenez/scripts_python/ssh/sshd_config","PROTOCOL 2")
append_last("/home/anjimenez/scripts_python/ssh/sshd_config","MACs umac-64-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com,hmac-sha1-etm@openssh.com,umac-64@openssh.com,umac-128@openssh.com,hmac-sha2-256,hmac-sha2-512,hmac-sha1")
append_last("/home/anjimenez/scripts_python/ssh/sshd_config","Ciphers aes128-ctr,aes192-ctr,aes256-ctr,blowfish-cbc,cast128-cbc,aes192-cbc,aes256-cbc")
##Add banner
banner = open("/etc/ssh/sshd-banner", "w")
for i in tbanner:
        banner.write(i + os.linesep)
banner.close()

##Restart sshd service
subprocess.call(["sysctl", "restart", "sshd"])


##add restart sshd service

##Enhance Kernel Parameters
for j in pkernel:
        append_last("sysctl.conf",j)
subprocess.call(["sysctl", "-p"])

##Remove unnecesary files
remove("/etc/hosts.allow")
remove("/etc/hosts.deny") 

##Hashing algorithm password store
subprocess.call(["authconfig", "--passalgo=sha512", "--update"])

##Parameters passwords
replaceALL(logindef)
