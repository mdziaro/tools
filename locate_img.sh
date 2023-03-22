#!/bin/bash
if [ $# = 0 ]; then
	echo "Error: You need to give at least one argument (filename)."
exit
fi
	if test -f $1; then
		cord=$(exiftool "$1" | grep "GPS Position" | tr  -s "deg" "°" | tr -d " " | awk -F ":" '{print $2}')
	    	if [ -n "$cord" ]; then
	    		echo "GPS Position:	"$cord
			if [ $2 = 1 ]; then
		    		xdg-open "https://www.google.com/maps/search/?api=1&query=$cord"
			fi
	    	else
			echo "GPS Position wasn't found in metadata."
	    	fi
	else
	    echo "File doesn't exist."
	fi
	exit
