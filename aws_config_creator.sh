#!/bin/sh

directory_name=/var/cache/netdata/.aws
directory_name=${directory_name}

if [ ! -d "$directory_name" ]; then
    echo "Directory making $directory_name"
	cp -a /var/lib/netdata/.aws "$directory_name"
fi
