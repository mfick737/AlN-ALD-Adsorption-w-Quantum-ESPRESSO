#!/bin/bash

cd /home/michael/Documents/AlN_Batch

loc='/home/michael/Documents/qe-6.7/bin/pw.x'

counter=0

for FILE in *
do
	echo $FILE
	if [ ${FILE: -3} == ".in" ]
	then
		NUM=${FILE//[!0-9]/}
		echo "Processing file: $FILE ..."
		eval "mpirun -np 4 ${loc} -inp $FILE > AlN_${NUM}.out"
	else
		echo "Not an .in file..."
	fi
	((counter=counter+1))
done

