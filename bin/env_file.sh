#!/bin/bash
for line in $(printenv)
do
    if [[ $line =~ ^env_.* ]]
    then 
        echo "${line:4}" >> "$HOME/.env"
    fi
done
