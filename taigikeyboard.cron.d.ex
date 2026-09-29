#
# Regular cron jobs for the taigikeyboard package.
#
0 4	* * *	root	[ -x /usr/bin/taigikeyboard_maintenance ] && /usr/bin/taigikeyboard_maintenance
