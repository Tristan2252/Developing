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

ffmpeg -i $filename -ss 00:00:01.000 -vframes 1 output.jpg
# add album art
python alb_add.py "$title.mp3" "output.jpg"

exit 0
