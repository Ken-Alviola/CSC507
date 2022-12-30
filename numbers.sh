#!/bin/bash

SECONDS=0

echo -n 'Start time: ' 
date

rm file1.txt

for ((i=0; i<=999999; i++))
do
    echo $RANDOM >> file1.txt    
done

echo -n 'End time: '
date

echo "Runtime: $SECONDS seconds"
