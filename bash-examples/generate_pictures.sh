#!/bin/bash

DIR="pictures"

if [ ! -d "$DIR" ]; then
    echo "Creating a directory: ./$DIR";
    mkdir "$DIR";
fi

echo "Generating dummy pictures.."
for i in {01..10}; do
    touch "$DIR/IMG_$i.JPG";
done
