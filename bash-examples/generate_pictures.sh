#!/bin/bash

if [ $1 ]; then
    DIR="$1";
else
    DIR="pictures";
fi

if [ ! -d "$DIR" ]; then
    echo "Creating a directory: ./$DIR";
    mkdir "$DIR";
fi

echo "Generating dummy pictures.."
for i in {01..10}; do
    dummy_pic="$DIR/IMG_$i.JPG";
    touch "$dummy_pic";
    if [ "$?" -eq 0 ]; then
        echo "... succesfully generated $dummy_pic";
    fi
done
