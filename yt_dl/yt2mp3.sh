#!/bin/bash

tmp_file=/tmp/ytdl
dl_quality="22"

# if command line arg exists set = to link
if [ $1 ]; then
	link=$1
else
	echo
	echo -n "Enter video link: "
	read link
fi

####  DOWNLOAD ####

mkdir "$tmp_file" # tmp file to store download
youtube-dl -f "$dl_quality" -o "$tmp_file/ytdl_out.%(ext)s" $link

# search any video format
file="$tmp_file/$(ls $tmp_file | grep '.wmv\|.avi\|.mp4\|.mkv')" # if video not found add .ext here

####  MP3 CONVERSION  ####

if ! [ -e $file ]; then
	printf "\nNeed File to convert, \nMake sure that the download is working correctly...\n\n"
	exit 0
fi

# get song info from usr
echo -n "Enter artist name: "
read artist
echo -n "Enter Song Title: "
read title
echo -n "Enter Album name: "
read album
echo -n "Enter Genre: "
read genre

# ffmpeg comand for converting to mp3
ffmpeg -i "$file" \
	-metadata title="$title" \
	-metadata artist="$artist" \
	-metadata album="$album" \
	-metadata genre="$genre" \
       	-b:a 192K -vn "$title.mp3"

# add album art
ffmpeg -i $file -ss 00:00:14.000 -vframes 1 output.jpg
python alb_add.py "$title.mp3" "output.jpg" # add album art with python

# cleaning up
rm -r "$tmp_file"
rm output.jpg  # album art file made by alb_add.py

exit 0
 


