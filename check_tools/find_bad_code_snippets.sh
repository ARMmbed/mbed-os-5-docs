#!/bin/bash

set -eo pipefail

mkdir -p BUILD
echo '*' > BUILD/.mbedignore

# simple fake main for snippets without a main function
cat > fake_main.c <<MAIN
#include "mbed_toolchain.h"
MBED_WEAK int main(void) { return 0; }
MAIN

function compile {
    if [ "$1" != "NOCI" -a "$1" != "TODO" ]
    then
        PYTHONPATH=mbed-os python mbed-os/tools/make.py -t GCC_ARM -m ${1:-K64F} --source=. --build=BUILD/${1:-K64F}/GCC_ARM | sed '/\(error\|warning\)/I!d'
    fi
}
     
for f in $(find -name mbed-os -prune -o -name '*.md' -print)
do
    # compile c++ snippets
    for l in $(sed -n '/``` *\(cpp\|c++\)\($\| \+\)/I=' $f)
    do
        echo "Validating cpp $f:$l ..."
        echo "#include \"mbed.h\"" > main.cpp
        sed -n $l',/```/{/```/d;p}' $f >> main.cpp
        compile "$(sed -n $l's/ *``` *\(cpp\|c++\)\($\| \+\)//Ip' $f)"
        rm main.cpp
    done
    
    # compile c snippets
    for l in $(sed -n '/``` *c\($\| \+\)/I=' $f)
    do
        echo "Validating c $f:$l ..."
        sed -n $l',/```/{/```/d;p}' $f > main.c
        compile "$(sed -n $l's/ *``` *c\($\| \+\)//Ip' $f)"
        rm main.c
    done

    # validate json snippets
    for l in $(sed -n '/``` *json\($\| \+\)/I=' $f)
    do
        echo "Validating json $f:$l ..."
        sed -n $l',/```/{/```/d;p}' $f > main.json
        if [ "$(sed -n $l's/ *``` *json\($\| \+\)//Ip' $f)" != "NO" ]
        then
            if sed -n '/ *"/q0;/ *[^ ]/q1' main.json
            then
                (echo "{" ; cat main.json ; echo "}") | python -m json.tool > /dev/null
            else
                cat main.json | python -m json.tool > /dev/null
            fi
        fi
        rm main.json
    done
done
