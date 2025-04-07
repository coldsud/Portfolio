#!/bin/bash

echo "Enter A filename:"

read filename

if [ -d "$filename" ]

then

    echo "Directory exists"

elif [ -f "$filename" ]

then

    echo "It is a regular file and the file exists"
    cat "$filename"

else

    echo "No such Directory or File"
    echo "Creating new file named "$filename"" 
    echo "Isaac Huston" > "$filename"
    echo "The contents of the newly created file $filename are:"
    cat "$filename"
     

fi