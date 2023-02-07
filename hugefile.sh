#!/bin/bash

SECONDS=0

echo -n 'Start time: ' 
date

rm hugefile1.txt
rm hugefile2.txt

for ((i=0; i<=999; i++))
do
    cat file1.txt >> hugefile1.txt
    cat file2.txt >> hugefile2.txt    
done

echo -n 'End time: '
date

echo "Runtime: $SECONDS seconds"
