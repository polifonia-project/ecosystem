#!/bin/bash
[[ -z "$1" ]] && echo "Message required" && exit 1

for d in content/* ; do
    cd "$d"
    pwd
    git add *
	git commit -m "$1"
	git push
    cd ../..
done

