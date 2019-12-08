#!/bin/bash -x
touch story/$1.md data/$1

cp test/skel.py "test/test_$1.py"
sed -i '' "s/Day1/Day$1/g"  "test/test_$1.py"

cp skel.py $1.py
sed -i '' "s/XXXXX/$1/g" "$1.py"