#!/usr/bin/python
#This script searches through manifest files in the /etc/puppet/modules directory 
#and checks to see if the files exist in the correct location.
import sys
import os
import subprocess
import re

if len(sys.argv)!=1:
    print "usage: puppet_module_checker"
    sys.exit()

#print manifest files
#find command and output to a temporary file
subprocess.call("find /etc/puppet/modules -iname '*.pp' > puppet_module_checker.tmp", shell=True)
#sub variable alias for filename
pmc="puppet_module_checker.tmp"

#search through modules *.pp file
#/etc/puppet/modules/*/manifests/*.pp
#open the temp file to read the init.pp file needed to find the source value
try:
    f = open(pmc, "r")
except IOError:
    print "couldn't open", pmc
    sys.exit()

lines = f.readlines()
for line in lines:
    line = line.rstrip("\n")    
    try:
        f2 = open(line, "r")
    except IOError:
        print "couldn't open", line
        sys.exit()
   
    print ("checking manifest " + line + "..."),
    lines = f2.readlines()
    for line in lines:
        line = line.rstrip("\n")
        #rid of beginning of line
        if re.search(r'^\s+', line):
            line = re.sub(r"^\s+", "", line)
        regex = re.findall(r"^source\s*=>\s*'puppet:///modules/[\d\D]+/[\d\D]+", line)
        if len(regex):
            #there may or may not be quotes?
            dirfile = re.findall(r"puppet:///modules/[\d\D]+/[\d\D]+[\w\d\._-]", line)
            dirfile = re.split(r"/+", dirfile[0]) #split forward slashes
            directory = dirfile[2]
            file = dirfile[3]
            source = "/etc/puppet/modules/"+directory+"/files/"+file
            #os module if file exists
            if os.path.isfile("/etc/puppet/modules/"+directory+"/files/"+file):
                print "done."
                done=1
            else:
                print ("\n Warning: " + source + " not found!"),
                done=0
    if done==0:
        print "\ndone."

f.close()
f2.close()

#remove pmc
os.remove(pmc)
sys.exit()
