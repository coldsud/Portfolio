#!/bin/bash

# Broadcast ID <network IP>

if [ $# -ne 1 ]; then
    echo "Usage: $0 <network_prefix>"
    exit 1
fi

# Total number of IPs in the range
total_ips=254

# Counter to keep track of processed IPs
processed_ips=0

# Start time of the sweep
start_time=$(date +%s)

# Function to print the progress message
print_progress() {
    current_time=$(date +%s)
    elapsed_time=$((current_time - start_time))
    remaining_ips=$((total_ips - processed_ips))
    remaining_time=$((remaining_ips * 30))
    echo "Still sweeping. $processed_ips IPs processed. Approx. $remaining_time seconds remaining."
}

if [ $# -ne 1 ]; then
    echo "Usage: $0 <network_prefix>"
    exit 1
fi

for ip in $(seq 1 254); do
    ping -c1 "$1.$ip" >> sweepresults.txt
    echo "Swept and written to sweepresults.txt for $1.$ip"
done

# Output the results after the loop completes
echo "Swept and written to sweepresults.txt. Below, is the dirt:"
cat sweepresults.txt | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" | sort -u