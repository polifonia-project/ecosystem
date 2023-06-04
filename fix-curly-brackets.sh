#!/bin/bash

[ -z "$1" ] && echo "Missing file argument" && exit 1

sed -i '' -e 's#{{#{% raw %}{{{% endraw %}#g' $1