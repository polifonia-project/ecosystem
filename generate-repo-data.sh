#!/bin/bash

rm _data/repositories.yml
while IFS= read -r line; do
    #
    IN="$line"
    arrIN=(${IN//:/ })
    repo=${arrIN[0]}
    treetype=${arrIN[1]}
    version=${arrIN[2]}
    echo "Text read from file: $line"
    echo "repo: $repo"
    echo "type: $treetype"
    echo "version: $version"
    echo "http://github.com/"$repo"/tree/"$version
    echo "https://raw.githubusercontent.com/"$repo"/"$version"/"
    echo "- repo: \"$repo\"" >> _data/repositories.yml
    echo "  type: \"$treetype\"" >> _data/repositories.yml
    echo "  version: \"$version\"" >> _data/repositories.yml
    echo "  url: \"http://github.com/$repo\"" >> _data/repositories.yml
    echo "  raw_link: \"https://raw.githubusercontent.com/$repo/$version/\"" >> _data/repositories.yml
done < repositories.txt