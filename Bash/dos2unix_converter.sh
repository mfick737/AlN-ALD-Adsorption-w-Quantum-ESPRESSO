#!/bin/bash

cd '/home/michael/Documents/Batch'

counter=0

for FILE in *
do
	if [ ${FILE: -3} == ".in" -o ${FILE: -4} == ".pbs" ]
	then 
		echo "Processing file: $FILE ..."
		eval "dos2unix $FILE"
	else
		echo "Not a .in file..."
	fi
	((counter=counter+1))
done
