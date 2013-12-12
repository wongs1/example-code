#!/usr/bin/python
#This prints host, fixed address, and hardware ethernet
import sys
import re

if len(sys.argv) != 1:
    print "usage: "+sys.argv[0]
    sys.exit()

input = "/etc/dhcp/dhcpd.conf"
try:
    f = open(input, "r")
except IOError:
    print "couldn't open " + input + ". try running as root"
    sys.exit()



lines = f.readlines()
clientnum=0
for line in lines:
    line = line.rstrip("\n")
    if re.search(r"host", line):
        line = re.sub(r"{", "", line) #gets rid of left bracket
        pieces = re.split(r"\s+", line) #split spaces into different lines
        host=pieces[1]
        if clientnum > 0:
            print ""
            print (host),
        else:
            print (host),
            clientnum+=1
    if re.search(r"fixed-address", line):
        regex = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line) #any line with ip address
        if re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line):
            print (regex[0]),
    if re.search(r"hardware ethernet", line):
        regex = re.findall(r"([\dA-Fa-f]{2}(?:[-:][\dA-Fa-f]{2}){5})", line)
        if re.findall(r"([\dA-Fa-f]{2}(?:[-:][\dA-Fa-f]{2}){5})", line):
            print (regex[0]),

f.close()
