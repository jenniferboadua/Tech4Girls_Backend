#!/bin/bash
n=$1
sum=0
for (( i=1 ; 1<=n ; i++ ))
do
sum= $(( $sum + i ))
done
echo "the sum of numbers from 1 to $n is: $sum"