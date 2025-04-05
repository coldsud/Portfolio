#!/bin/bash
#
#
filename=$1

if [ -f "$filename" ] && [ -w "filename" ]
then
	echo "Hello" >$filename
else
	touch "$filename"
	echo "Hello" > $filename
fi
