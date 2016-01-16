#!/bin/bash

INSTALL_DIR="/usr/local/bin"

HOMEBREW="/usr/local/bin/brew"
EYED3="/usr/local/lib/python2.7/site-packages/eyed3"
FFMPEG="/usr/local/bin/ffmpeg"

yt2mp3_install ()
{
	cp yt2mp3.sh $INSTALL_DIR/yt2mp3
	cp alb_add.py $INSTALL_DIR/alb_add
	
	if [ -e $INSTALL_DIR/alb_add ]; then
		printf "\nalb_add installed\n"
	elif [ -e $INSTALL_DIR/yt2mp3 ]; then
		printf "\nYt2mp3 installed\n"
	fi
}

hb_install ()
{
	while [ 1 ]; do
		echo -n "Homebrew is needed to run installer, would you like to install it [Y/N]: "
		read opt
		if [ $opt == "N" ]; then
			exit 0
		elif [ $opt == "Y" ]; then
			ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
			printf "\n\nHomebrew Installed\n"
			printf "Learn more about homebrew at: \n"
			printf "https://github.com/Homebrew/homebrew/tree/master/share/doc/homebrew#readme\n\n"
			break
		else
			printf "\n\n**** Invalid Input: $opt ****"
		fi
	done
}

eyed3_install ()
{
	brew install eyeD3
	if [ -e $EYED3 ]; then # make sure it installed
		printf "\neyeD3 installed\n"
	fi
}

ffmpeg_install ()
{
	brew install ffmpeg
	if [ -e $FFMPEG ]; then # make sure it installed
		printf "\nffmpeg installed\n"
	fi
}


darwin_install (){
	
	if ! [ -e $HOMEBREW ]; then
		hb_install
	fi

	if ! [ -e $EYED3 ]; then
		eyed3_install
	fi

	if ! [ -e $FFMPEG ]; then
		ffmpeg_install
	fi
	
	yt2mp3_install
}

if [ $(uname -s) == "Darwin" ]; then
	darwin_install
elif [ $(uname -s) == "Linux" ]; then
	echo
fi

#ppa:mc3man/trusty-media
