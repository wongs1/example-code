#!/bin/bash
#This searches the specified string for processes.
if [ $# -ne 1 ]
then
	echo "usage: $0 STRING"
	exit 1
fi

answer=`ps -ef | grep $1 | grep -v grep | grep -v $0`
line=`ps -ef | grep $1 | grep -v grep | grep -v $0 | wc -l`
if [ $line -ge 1 ]
then
	ps -ef | head -n 1
	echo $answer
fi
