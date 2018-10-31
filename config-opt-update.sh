#!/bin/bash

path="docs/reference/configuration/"

find $path -name '*.md' | while read filepath; do
    file=`echo "$filepath" | cut -d '.' -f1 | cut -d '/' -f4 | tr '[:upper:]' '[:lower:]'`
    echo "$filepath"
    echo "$file"
    
    grep "\`\`\`" $filepath > /dev/null

    if [ $? -eq 0 ]; then
        config=`mbed compile --config -v --prefix "$file" -m K64F -t GCC_ARM | sed -n '/Macros/q;p'`
   
        updated_file=$(perl -0777 -pe 's/```(.*?)```/```\n$ARGV[0]\n```/gs' "$filepath" "$config")

        cat /dev/null > $filepath
        echo "$updated_file" > $filepath
    else
        echo "Skipping"
    fi
done
