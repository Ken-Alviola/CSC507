#!/bin/bash

rm ten_mil.txt

SECONDS=0

echo -n 'Start time: ' 
date

while read -r number
do
    let "number *=2"
    echo $number >> ten_mil.txt
done < file2.txt

echo -n 'End time: '
date

echo "Runtime: $SECONDS seconds"