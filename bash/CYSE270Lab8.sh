#!/bin/bash

#pompt for numeber
ten=10
echo "Enter the number to check: "

read check

if [ $check -gt $ten ]

then

echo "input number is greater than 10"

else

echo "input number is not greater than 10"

fi