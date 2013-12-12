#!/usr/bin/python
#This script port forwards from the arguments provided
import sys
import re
import subprocess

if len(sys.argv)!=4:
    print "usage: port_forward port proto destination where port can be either a service name from /etc/services or a numbered port, and proto is either tcp or udp"
    sys.exit()

port=sys.argv[1]
proto=sys.argv[2]
dest=sys.argv[3]

if proto != "tcp" and proto != "udp":
    print "protocol must be either tcp or udp"
    sys.exit()

portnumfound=0
if re.search(r"^\d+$", port):
    portnumfound=1
    portnum=port
else:
    try:
        f = open("/etc/services", "r")
    except IOError:
        print "couldn't open /etc/services"
        sys.exit()
    #take into account comments and names ending with port name
    #check for valid protocol
    lines = f.readlines()
    for line in lines:
        line = line.rstrip("\n")
        #remember to remove spaces at beginning just in case
        if re.search(r'^\s+', line):
            line = re.sub(r"^\s+", "", line)
        #field 1 name, field 2 portnum/proto
        regex= re.findall(r"^"+port+'\s+\d+\/'+proto, line)
        if len(regex):
            #line = re.sub(r"CHANGE_USERNAME_HERE", USERNAME, line)
            portnumfound=1
            portnum=regex[0]
            
            #extract number from portnum
            #get rid of beginning of portnum
            portnum = re.sub(r"^"+port+'\s+', "", portnum)
            #get rid of end of portnum
            portnum = re.sub(r"\/"+proto, "", portnum)
            
            
    f.close()

if portnumfound == 0:
    print "port name " + port + " not found in /etc/services"
    sys.exit()

#run iptables command and save it
#variables portnum proto dest
subprocess.call("iptables -t nat -I PREROUTING -i eth0 -p " + proto + " -m " + proto + " --dport " + portnum + " -j DNAT --to-destination " + dest, shell=True)
subprocess.call("iptables -I FORWARD -i eth0 -p " + proto + " -m " + proto + " --dport " + portnum + " -j ACCEPT", shell=True)
subprocess.call("iptables-save > /etc/sysconfig/iptables", shell=True)

sys.exit()
