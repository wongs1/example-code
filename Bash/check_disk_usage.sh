#!/bin/bash
#This checks disk usage and warns the user if
#utilization percent is 90% or more.
TEMP=`mktemp`
usage=`df -hP | grep '^/dev' > $TEMP`

while read line
do
	percent=`echo "$line" | awk '{print $5}' | sed -r 's/%//g'`
	memavail=`echo "$line" | awk '{print $4}'`
	dir=`echo "$line" | awk '{print $6}'`
	if [ $percent -ge 90 ]
	then
		echo "Warning: $dir is at $percent% utilization, with only $memavail left."
	fi
done < "$TEMP"
rm $TEMP
