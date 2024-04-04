#!/bin/bash

# Check if the correct number of arguments is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <network_prefix>"
    exit 1
fi

# Loop over the IP addresses in the range 1 to 254
for ip in $(seq 1 254); do
    # Execute ping command in background
    ping -c 1 "$1.$ip" | grep -q "bytes from" && echo "$1.$ip" &
done
