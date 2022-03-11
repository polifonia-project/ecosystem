#!/bin/bash

for d in content/* ; do
    cd "$d"
    pwd
    git pull
    cd ../..
done
