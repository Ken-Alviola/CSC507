#!/bin/bash

rm newfile1.txt

SECONDS=0

echo -n 'Start time: ' 
date

while read -r number
do
    let "number *=2"
    echo $number >> newfile1.txt
done < file1.txt

echo -n 'End time: '
date

echo "Runtime: $SECONDS seconds"
