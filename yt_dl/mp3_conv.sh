#!/bin/bash

if ! [ -e $1 ]; then
	printf "\nNeed File to convert\n\n"
	exit 0
fi

filename=$1

echo -n "Enter artist name: "
read artist
echo -n "Enter Song Title: "
read title

ffmpeg -i "$filename" \
	-metadata title="$title" \
	-metadata artist="$artist" \
       	-b:a 192K -vn "$title.mp3"

