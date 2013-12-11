#!/bin/bash
#This displays information about the user.
name=`grep $USERNAME /etc/passwd | cut -d ':' -f 5`
current_time=`date "+%l:%M%P"`
echo "Welcome to $HOSTNAME, $name!"
echo "You are logged in as $USERNAME and your current directory is $PWD."
echo "The time is $current_time "
