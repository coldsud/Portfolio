import socket
import json
import os
from cryptography.fernet import Fernet

# -------------------- Configuration -------------------- #

HOST = '0.0.0.0'  # Server IP address (0.0.0.0 listens on all interfaces)
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
        send_encrypted(client, "Login successful!\n")
        return True
    else:
        send_encrypted(client, "Invalid credentials.\n")
        return False

# -------------------- Encryption Functions -------------------- #

def send_encrypted(client, message):
    """Encrypt and send a message to the client."""
    encrypted_message = cipher_suite.encrypt(message.encode())
    client.sendall(encrypted_message)

def receive_encrypted(client):
    """Receive and decrypt a message from the client."""
    encrypted_message = client.recv(BUFSIZE)
    try:
        decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    except:
        decrypted_message = ""
    return decrypted_message

# -------------------- File Transfer Functions -------------------- #

def receive_file(client):
    """Receive an encrypted file from the client and save it."""
    send_encrypted(client, "Enter the filename to upload:")
    filename = receive_encrypted(client)
    send_encrypted(client, "Ready to receive the file.")
    status = receive_encrypted(client)
    if status != "ready":
        send_encrypted(client, "File transfer cancelled.")
        return
    # Receive the encrypted file data length
    data_length_str = client.recv(BUFSIZE).decode()
    client.send(b'ACK')  # Send acknowledgment
    try:
        data_length = int(data_length_str)
    except ValueError:
        send_encrypted(client, "Failed to receive file size.")
        return
    # Receive the encrypted file data
    encrypted_data = b''
    while len(encrypted_data) < data_length:
        chunk = client.recv(BUFSIZE)
        if not chunk:
            break
        encrypted_data += chunk
    try:
        file_data = cipher_suite.decrypt(encrypted_data)
    except:
        send_encrypted(client, "Failed to decrypt file data.")
        return
    file_path = os.path.join(SERVER_FILES_DIR, filename)
    with open(file_path, 'wb') as f:
        f.write(file_data)
    send_encrypted(client, "File uploaded successfully.")

def send_file(client):
    """Send an encrypted file to the client."""
    files = os.listdir(SERVER_FILES_DIR)
    if not files:
        send_encrypted(client, "No files available for download.")
        return
    # Send available files
    file_list = "Available files:\n" + '\n'.join(files)
    send_encrypted(client, file_list)
    send_encrypted(client, "Enter the filename to download:")
    # Receive filename
    filename = receive_encrypted(client)
    if filename not in files:
        send_encrypted(client, "File not found.")
        return
    send_encrypted(client, "Preparing to send the file.")
    # Read and encrypt the file data
    file_path = os.path.join(SERVER_FILES_DIR, filename)
    with open(file_path, 'rb') as f:
        file_data = f.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    # Send the length of the encrypted data
    data_length = len(encrypted_data)
    client.sendall(str(data_length).encode())
    ack = client.recv(BUFSIZE)  # Wait for acknowledgment
    # Send the encrypted data
    client.sendall(encrypted_data)
    # Wait for acknowledgment
    ack = client.recv(BUFSIZE)
    send_encrypted(client, "File sent successfully.")

def handle_file_transfer(client):
    """Handle file upload/download requests from the client."""
    while True:
        send_encrypted(client, "Do you want to (1) Upload or (2) Download a file? Enter 1, 2 or 'exit' to quit:")
        choice = receive_encrypted(client)
        if choice == '1':
            receive_file(client)
        elif choice == '2':
            send_file(client)
        elif choice.lower() == 'exit':
            send_encrypted(client, "Goodbye!")
            client.close()
            print("Client has disconnected.")
            break
        else:
            send_encrypted(client, "Invalid choice. Please try again.")

# -------------------- Client Handling -------------------- #

def handle_client(client, address, users):
    """Handle the client connection, authentication, and file transfers."""
    print(f"Connected from: {address}")
    send_encrypted(client, "Welcome to the server!")
    authenticated = False
    while not authenticated:
        send_encrypted(client, "Do you want to (1) Register or (2) Login? Enter 1 or 2:")
        choice = receive_encrypted(client)
        if choice == '1':
            authenticated = register_user(client, users)
        elif choice == '2':
            authenticated = login_user(client, users)
        else:
            send_encrypted(client, "Invalid choice. Please enter 1 or 2.\n")
    # After successful authentication, handle file transfer
    handle_file_transfer(client)

# -------------------- Main Server Loop -------------------- #

def main():
    """Main function to start the server and handle incoming connections."""
    users = load_users()
    print(f"Server started at {HOST}:{PORT}")
    server = socket.socket()
    server.bind(ADDRESS)
    server.listen()
    try:
        while True:
            print("Waiting for connection...")
            client, address = server.accept()
            handle_client(client, address, users)
    except KeyboardInterrupt:
        print("\nServer shutting down.")
    finally:
        server.close()

if __name__ == "__main__":
    main()

