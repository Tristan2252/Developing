#!/bin/bash

if [ $1 ]; then 
	ls_out=$(ls -l $1)
else
	echo "Testable File Name needed"
	exit 1
fi

date_out=$(date)


file_time=$(./slice_parce -s 5 -e 7 -i "$ls_out")
date_time=$(./slice_parce -s 1 -e 4 -i "$date_out")

echo "$file_time"
echo "$date_time"

exit 0
