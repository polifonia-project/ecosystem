#!/bin/bash

for d in */ ; do
    cd "$d"
    pwd
    git pull
    cd ..
done
