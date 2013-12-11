#!/bin/bash
#This greps for kernel processes
#Argument '-v' will grep for nonkernel processes
if [ $# -eq 0 ]
then
	ps -ef | grep '[[:digit:]] \[' # greps kernel processes
elif [ $# -eq 1 ]
then
	if [ $1 = -v ]
	then
		ps -ef | grep -v '[[:digit:]] \[' | grep -v grep # greps non kernel processes
	else
		echo "Enter -v as argument."
		exit 1
	fi
else
	echo "need 0 or 1 arguments."
	exit 1
fi
