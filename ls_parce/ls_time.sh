#!/bin/bash

ls_out=$(ls -al)
date_out=$(date)

file_time=$(echo "$ls_out" | ./slice_parce)
date_time=$(echo "$date_out" | ./slice_parce)

echo "$file_time\n"
echo "$date_out\n"

exit 0
