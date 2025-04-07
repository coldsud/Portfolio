#!/bin/bash

echo "Enter your name:"

read name

echo "Thank you $name for choosing to complete the extra credit for 15 points"

echo "$name Please enter the name of a directory: you would like to view the contents of"

read directory

if [ -d "$directory" ]

then

echo "$directory Contents consist of"

ls -l "$directory"

else

echo "Sorry, the entered directory name is not a valid directory name"

fi
