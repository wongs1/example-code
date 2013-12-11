#!/bin/bash
#This script gets information about the network.
ipv4=`/sbin/ifconfig eth0 | grep 'inet addr' | cut -d ':' -f 2 | cut -d ' ' -f 1`
mac=`/sbin/ifconfig eth0 | grep 'HWaddr' | cut -d ' ' -f 11`
gateway=`/sbin/route | grep 'default' | cut -d ' ' -f 10`
Nspeed=`/sbin/ethtool eth0 | grep 'Speed' | cut -d : -f 2 | cut -d ' ' -f 2`
Nduplex=`/sbin/ethtool eth0 | grep 'Duplex' | cut -d ':' -f 2 | cut -d ' ' -f 2`

echo "IPv4 address: $ipv4" 
echo "MAC address: $mac" 
echo "Gateway router: $gateway"

dnss=`cat /etc/resolv.conf | grep 'nameserver' | grep -v 'nameservers'`
for word in $dnss; do
	if [ $word = 'nameserver' ]
	then
		dnsscount=1
	fi
	if [ $dnsscount -ne 1 ]
	then
		echo "DNS server: $word"
	fi
	dnsscount=$(($dnsscount+1))

done

dnsdcount=1
dnsd=`cat /etc/resolv.conf | grep 'search'`
for word in $dnsd; do
	if [ $dnsdcount -ne 1 ]
	then
		echo "DNS domain: $word"
	fi
	dnsdcount=$(($dnsdcount+1))
done

echo "NIC speed: $Nspeed"
echo "NIC duplex: $Nduplex"
