#!/bin/bash
#This creates up to 3 backups for use with a cron job.
if [ -e /backups/home.bkup.2 ]
then
	rm /backups/home.bkup.2
fi
if [ -e /backups/home.bkup.1 ]
then
	mv /backups/home.bkup.1 /backups/home.bkup.2
fi
if [ -e /backups/home.bkup ]
then
	mv /backups/home.bkup /backups/home.bkup.1
fi
/sbin/dump -0 -f /backups/home.bkup /home
