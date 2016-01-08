#!/bin/bash

file=$1
date_out=$(./slice_parce -s 0 -e 1 -i "$(date)" -d :) # gettig rid of the seconds

# getting file stats from ls -l
if [ $file ]; then 
	ls_out=$(ls -l $file)
else
	echo "Testable File Name needed"
	exit 1
fi

file_date=$(./slice_parce -s 7 -e 7 -i "$ls_out")
sys_date=$(./slice_parce -s 3 -e 3 -i "$date_out")

file_time=$(./slice_parce -s 8 -e 8 -i "$ls_out")
sys_time=$(./slice_parce -s 4 -e 4 -i "$date_out")

time_dif="$(./comp -d $sys_date,$file_date) $(./comp -t $sys_time,$file_time)"

echo ""
echo "File date: $(./slice_parce -s 5 -e 8 -i "$ls_out")"
echo "System date: $(./slice_parce -s 1 -e 4 -i "$date_out")"
echo "File '$file' is $time_dif older then current system time"
echo ""

exit 0
