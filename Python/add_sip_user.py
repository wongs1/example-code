#!/usr/bin/python
#This script automates the process of adding a new user to an Asterisk server.
import sys
import re
import subprocess
import shutil

if len(sys.argv)!= 4:
    print "usage: add_sip_user.py username fullname email"
    sys.exit()

username=sys.argv[1]
fullname=sys.argv[2]
email=sys.argv[3]


#add the appropriate values to bottom of the sip.conf, extensions.conf, and voicemail.conf files
#determine which extension to use starting at 4001
try:
#test before using on real file
    f = open("/etc/asterisk/extensions.conf", "r")
except IOError:
    print "couldn't open extensions.conf"
    sys.exit()


lines = f.readlines()
min = 4001
newextension = 4001
for line in lines:
    line = line.rstrip("\n")
    if re.search(r"^\s+", line):
        line = re.sub(r"^\s+", "" , line)
    regex = re.findall(r'^exten\s*=>\s*[\d]+', line)
    if len(regex):
        regex = re.findall(r'[\d]+', regex[0])
        extension = regex[0]
        if int(extension) >= min:
            #set new extension to highest number above 4000
            if int(extension) >= newextension:
                newextension=int(extension)+1
f.close()
newextension=str(newextension)

#set SIP password to email addy and voicemail PIN to reverse extension
SIPpw=email
reversePin = str(newextension)[::-1]

#assume username is unique
#make sure to append

#extensions.conf
try:
    f = open("/etc/asterisk/extensions.conf", "a")
except IOError:
    print "couldn't open extensions.conf"
    sys.exit()

f.write("exten => " + newextension + ",1,Dial(SIP/" + username + ", 20)\n same => n,VoiceMail(" + newextension + "@user-voicemail, u)\n")
f.close()


#sip.conf
try:
    f = open("/etc/asterisk/sip.conf", "a")
except IOError:
    print "couldn't open extensions.conf"
    sys.exit()

f.write("[" + username + "]\ntype=friend\nhost=dynamic\nsecret=" + email + "\ncontext=users\ndisallow=all\nallow=ulaw\nallow=alaw\nallow=gsm\n")
f.close()


#voicemail.conf
try:
    f = open("/etc/asterisk/voicemail.conf", "a")
except IOError:
    print "couldn't open extensions.conf"
    sys.exit()

f.write("" + newextension + " => " + reversePin + "," + fullname + "," + email + "," + email + ",attach=yes|tz=eastern\n")

f.close()

#tell asterisk to re-read them
#asterisk -rx "COMMAND"
#reload SIP, dialplan, and voicemail
subprocess.call("asterisk -rx 'dialplan reload' > /dev/null", shell=True)
subprocess.call("asterisk -rx 'sip reload' > /dev/null", shell=True)
subprocess.call("asterisk -rx 'voicemail reload' > /dev/null", shell=True)

print "Added " + username + " at " + newextension + " with PIN " + reversePin
