#!/bin/bash

if [ $1 ]; then 
	ls_out=$(ls -l $1)
else	
	ls_out=$(ls -l $1 | sed -n '1!p') # sed removes total line from ls output
fi

date_out=$(date)


file_time=$(echo "$ls_out" | ./slice_parce)
date_time=$(echo "$date_out" | ./slice_parce)

echo "$file_time"
echo "$date_out"

exit 0
