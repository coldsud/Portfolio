#!/bin/bash

# Function to extract network prefix from IP address
get_network_prefix() {
    local ip="$1"
    echo "${ip%.*}"
}

# Get the IP address of the host
ip_address=$(hostname -I | awk '{print $1}')

# Check if an IP address is obtained
if [ -z "$ip_address" ]; then
    echo "Failed to retrieve IP address. Please check your network connection."
    exit 1
fi

# Extract the network prefix
network_prefix=$(get_network_prefix "$ip_address")

# Print the network prefix
echo "Network prefix: $network_prefix"

# Function to perform ping sweep for a given IP address
ping_sweep() {
    local ip="$1"
    ping -c 1 -w 1 "$ip" >/dev/null 2>&1 && echo "$ip"
}

# Loop over the IP addresses in the range 1 to 254
for ip in $(seq 1 254); do
    # Execute ping_sweep function in background
    ping_sweep "$network_prefix.$ip" &
done
