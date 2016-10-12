#!/bin/bash

while read ip; do
    contents=$(curl "$ip")
    if [[ ! -z $contents ]]; then
        echo $ip
    fi
done < "onion.txt"
