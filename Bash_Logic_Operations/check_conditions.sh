#!/bin/bash
#script to check AND, OR and NOT conditions
Number1=$1
Number2=$2

#to check if both numbers are greater than 10
if [[ $Number1 -gt 10 && $Number2 -gt 10 ]]
then 
echo "both numbers are greater than 10"
elif [[ $Number1 -gt 10 || $Number2 -gt 10 ]]
then 
echo "at least one number is greater than 10"
else
echo "neither number is greater than 10"
fi