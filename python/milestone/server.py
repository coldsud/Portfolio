
import socket
import json
import os
from cryptography.fernet import Fernet

# -------------------- Configuration -------------------- #

HOST = '10.0.0.251'  # Server IP address (0.0.0.0 listens on all interfaces)
PORT = 5002
BUFSIZE = 4096
ADDRESS = (HOST, PORT)

# File paths
USERS_FILE = 'users.json'
KEY_FILE = 'key.key'
SERVER_FILES_DIR = 'server_files'

# Ensure the server_files directory exists
os.makedirs(SERVER_FILES_DIR, exist_ok=True)

# -------------------- Encryption Setup -------------------- #

def load_key():
    """Load the encryption key from the key.key file."""
    if not os.path.exists(KEY_FILE):
        # Generate a new key and save it
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as key_file:
            key_file.write(key)
    else:
        with open(KEY_FILE, 'rb') as key_file:
            key = key_file.read()
    # Validate the key length
    if len(key) != 44:
        raise ValueError("Invalid Fernet key length.")
    return key

# Initialize Fernet cipher
key = load_key()
cipher_suite = Fernet(key)

# -------------------- User Management -------------------- #

def load_users():
    """Load user credentials from the users.json file."""
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, 'r') as f:
        try:
            users = json.load(f)
        except json.JSONDecodeError:
            users = {}
    return users

def save_users(users):
    """Save user credentials to the users.json file."""
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)

def register_user(client, users):
    """Handle user registration."""
    send_encrypted(client, "Enter a username:")
    username = receive_encrypted(client)
    if username in users:
        send_encrypted(client, "Username already exists. Try logging in.\n")
        return False
    send_encrypted(client, "Enter a password:")
    password = receive_encrypted(client)
    users[username] = password
    save_users(users)
    send_encrypted(client, "Registration successful!\n")
    return True

def login_user(client, users):
    """Handle user login."""
    send_encrypted(client, "Enter your username:")
    username = receive_encrypted(client)
    send_encrypted(client, "Enter your password:")
    password = receive_encrypted(client)
    if username in users and users[username] == password:
