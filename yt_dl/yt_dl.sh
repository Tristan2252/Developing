#!/bin/bash

tmp_file=/tmp/ytdl

if [ $1 ]; then
	link=$1
else
	echo -n "Enter video link: "
	read link
fi

# LINUX
if [ "$(uname -s)" == "Linux" ]; then
	mkdir "$tmp_file"
	youtube-dl -o "$tmp_file/ytdl_out.%(ext)s" $link
	
	file=$(ls $tmp_file | grep '.wmv\|.avi\|.mp4') # search any video formati
	./mp3_conv.sh "$tmp_file/$file"

	exit 0

fi

# MAC OS X
if [ "$(uname -s)" == "Darwin" ]; then
	mkdir "$tmp_file"
	youtube-dl -o "$tmp_file/ytdl_out.%(ext)s" $link
	
	file=$(ls $tmp_file | grep '.wmv\|.avi\|.mp4\|.mkv') # search any video formati
	./mp3_conv.sh "$tmp_file/$file"

	exit 0
fi
