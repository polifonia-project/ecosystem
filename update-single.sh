#!/bin/bash

update="$1"

[ "$update" ] || echo "Give repo as \"org/repo\"" 
[ "$update" ] || exit 1

echo "Updating "$update
#echo "SHIT"

#exit()

while IFS= read -r line; do
    #
    IN="$line"
    arrIN=(${IN//:/ })
    repo=${arrIN[0]}
    version=${arrIN[2]}
    #
    if [ "$repo" == "$update" ]; then
        echo "Text read from file: $line"
        echo "repo: $repo"
        echo "version: $version"
        rm -rf "content/_$repo"
        git clone -n "https://github.com/$repo" "content/_$repo"
        cd "content/_$repo"
        git ls-tree -r "$version" --full-tree --name-only | grep "\.md" > files.tmp
        while IFS= read -r line; do
            git checkout "$version" "$line"
        done < files.tmp
        rm files.tmp
        rm -rf .git
        cd -
    else
        echo "Skipping $repo"
    fi
done < repositories.txt