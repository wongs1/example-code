#!/bin/bash
#This finds the MAC address of computers in the local area network.
if [ $# -ne 1 ]
	then
	echo "usage: $0 IP"
	exit 1
fi

ip=`echo $1 | grep -Eo "^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$"`
if [ -z $ip ]
then
	echo "that is not an IP address!"
	exit 1
fi

LAN=`echo $ip | cut -d '.' -f 4`

if [ "$ip" != "10.0.2.$LAN" ]
then
	echo "this only works for IPs in the LAN!"
	exit 1
fi

ping $ip -c 1 > /dev/null
arpinc=`arp -n | grep $ip | awk '{print $2}'`
if [ "$arpinc" = "(incomplete)" ]
then
	echo "$ip did not respond to ping"
	exit 1
fi

gip=`arp -n | grep $ip | awk '{print $3}'`
echo "$gip"
