#!/bin/bash

DIR="pictures"

if [ ! -d "$DIR" ]; then
    echo "Creating a directory: ./$DIR";
    mkdir "$DIR";
fi

touch "$DIR/IMG_00.JPG";
