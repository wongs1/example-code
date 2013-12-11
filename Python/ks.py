#!/usr/bin/python
#This script assists in the Kickstart configuration process
import sys
import re

if len(sys.argv) != 3:
    print "usage: ks hostname mac_addy"
    sys.exit()
hostname=sys.argv[1]
macaddr=sys.argv[2]

#check for valid mac address before opening
if re.search(r"(^[\dA-Fa-f]{2}(?:[-:][\dA-Fa-f]{2}){5}$)", macaddr):
    #replace ':' with '-'
    #make lowercase and add 01 to beginning
    fmac = "01-"+(re.sub(r":", "-", macaddr))
    fmac=fmac.lower()
else:
    print "not valid mac address. example: 11:22:33:AA:BB:CC"
    sys.exit()

try:
    f = open("/export/centos64/template.ks.cfg", "r")
except IOError:
    print "couldn't open template.ks.cfg"
    sys.exit()

try:
    k = open("/export/centos64/"+hostname+".ks.cfg", "w")
except IOError:
    print "couldn't open",sys.argv[1]
    sys.exit()

lines = f.readlines()
for line in lines:
    line = line.rstrip("\n")
    if re.search(r'CHANGE_HOSTNAME_HERE', line):
        line = re.sub(r"CHANGE_HOSTNAME_HERE", hostname, line)
    k.write(line)
    k.write("\n")
f.close()
k.close()

try:
    f = open("/tftpboot/pxelinux.cfg/template", "r")
except IOError:
    print "couldn't open template"
    sys.exit()

try:
    k = open("/tftpboot/pxelinux.cfg/"+fmac, "w")
except IOError:
    print "couldn't open",fmac
    sys.exit()

lines = f.readlines()
for line in lines:
    line = line.rstrip("\n")
    if re.search(r'CHANGE_HOSTNAME_HERE', line):
        line = re.sub(r"CHANGE_HOSTNAME_HERE", hostname, line)
    k.write(line)
    k.write("\n")
f.close()
k.close()
