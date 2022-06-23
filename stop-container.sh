#!/usr/bin/env bash

if [[ -z "${1}" ]]; then 
    echo "You must provide at least one port, or all for all containers"; 
    exit 0
fi

if [[ "${1}" == "all" ]]; then
    for id in $(docker ps -q)
        do
            if ! [[ $(docker port "${id}") == *"8081"* ]]; then
                echo "stopping container ${id}"
                docker stop "${id}"
            fi
        done
        exit 0
fi

for port in "$@"
    do
        for id in $(docker ps -q)
            do
                if ! [[ $(docker port "${id}") == *"8082"* ]] && [[ $(docker port "${id}") == *"${port}/tcp"* ]]; then
                    echo "stopping container ${id}"
                    docker stop "${id}"
                fi
            done 
    done

exit 0
