#!/bin/bash
#This lists the services of a specified run level
if [ $# -ne 1 ]
then
	echo "usage: $0 run_level"
	exit 1
fi

#checks to see that it is a number, not a letter or symbol
digitcheck=`echo $1 | egrep ^[0-6]$`
if [ -z $digitcheck ]
then
	echo "$1 is not a valid run level!"
	exit 1
fi

run_level=$1 #used as alias
chkconfig --list | grep "$run_level:on" | awk '{print $1}'
