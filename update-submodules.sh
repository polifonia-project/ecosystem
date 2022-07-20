#!/bin/bash

# for d in content/* ; do
#     cd "$d"
#     pwd
#     git pull
#     cd ../..
# done

# for d in content/* ; do
#     cd "$d"
#     pwd
#     git pull
#     cd ../..
# done

while IFS= read -r line; do
    echo "Text read from file: $line"
	IN="$line"
	arrIN=(${IN//:/ })
	repo=${arrIN[0]}
	version=${arrIN[2]}
	echo "repo: $repo"
	echo "version: $version"     
	[ -d "content/$repo" ] || git clone -n "https://github.com/$repo" "content/$repo"
	cd "content/$repo" 
	git ls-tree -r "$version" --full-tree --name-only | grep "\.md" > files.tmp
	while IFS= read -r line; do 
		git checkout "$version" "$line"
	done < files.tmp
	rm files.tmp
	cd -
done < repositories.txt