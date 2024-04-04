#!/usr/bin/env python3
import subprocess
import ipaddress
import netifaces
import sys
from multiprocessing import Pool

# Function to extract network prefix from IP address
def get_network_prefix(ip):
    ip = ipaddress.ip_interface(ip)
    return ip.network.network_address

# Function to perform ping sweep for a given IP address
def ping_sweep(ip):
    result = subprocess.run(['ping', '-c', '1', '-W', '1', str(ip)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode == 0:
        print(ip)

# Get the IP address of the host
ip_address = None
for interface in netifaces.interfaces():
    addresses = netifaces.ifaddresses(interface).get(netifaces.AF_INET)
    if addresses is not None:
        for address in addresses:
            if 'addr' in address and not ipaddress.ip_address(address['addr']).is_loopback:
                ip_address = address['addr']
                break
    if ip_address:
        break

if not ip_address:
    print("Failed to retrieve IP address. Please check your network connection.")
    sys.exit(1)

# Extract the network prefix
network_prefix = get_network_prefix(ip_address)

# Print the network prefix
print("Network prefix:", network_prefix)

# Create a pool of worker processes
pool = Pool()

# Loop over the IP addresses in the range 1 to 254 within the same network prefix
ip_addresses = [str(network_prefix) + "." + str(ip_suffix) for ip_suffix in range(1, 255)]

# Perform ping sweep asynchronously
for ip in ip_addresses:
    pool.apply_async(ping_sweep, (ip,))

# Close the pool to prevent further tasks from being submitted
pool.close()

# Wait for the worker processes to complete
pool.join()
