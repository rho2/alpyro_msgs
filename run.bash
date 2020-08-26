#!/bin/bash
set -e

docker build . -t alpyro_gen:latest

docker run -it -v $PWD/alpyro_msgs:/out alpyro_gen

for D in alpyro_msgs/*; do
    if [ -d "${D}" ]; then
        echo "${D}"
        sudo chown -R $UID:$UID "${D}"
        chmod 775 "${D}"
        chmod 664 "${D}"/*
    fi
done
