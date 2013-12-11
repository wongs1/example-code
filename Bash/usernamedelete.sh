#!/bin/bash
#This reads a list and deletes all usernames
#from the list.
while read username; do
	sudo /usr/sbin/userdel -r $username
done
