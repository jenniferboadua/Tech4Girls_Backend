#!/bin/bash
# Script to check if a number is odd or even
echo "Input the number"
read Number
if (($Number % 2 == 0))
then
echo "The number $Number is even"
else
echo "The number $Number is odd"
fi