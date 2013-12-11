#!/bin/bash
#This script prints all processes owned by the specified user
if [ $# -ne 1 ]
then
	echo "usage: $0 user"
	exit 1
fi

#greps for all valid characters.
#Characters can be uppercase letters, lowercase letters, digits, underscores, and dashes
#First character must be a letter or underscore
#If any invalid characters are shown, then empty string
validusername=`echo $1 | egrep ^[A-Za-z_][A-Za-z0-9_-]+$`
#if empty string, then exit
if [ -z $validusername ]
then
	echo "$1 is not a valid username!"
	exit 1
fi

username=$1 #alias
eusername=`egrep ^$username: /etc/passwd | cut -d ':' -f 1`

if [ "$eusername" = "" ]
then
	echo "$username is not a user name on this system!"
	exit 1
fi

#use ps to print all processes owned by user
PID=`ps -ef | grep $eusername | grep -v grep | grep -v $0 | awk '{print $2, $8}'`
echo "$PID"
