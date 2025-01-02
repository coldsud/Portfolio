import socket
import os
from cryptography.fernet import Fernet

# -------------------- Configuration -------------------- #

HOST = '10.0.0.251'  # Server IP address
PORT = 5002
BUFSIZE = 4096
ADDRESS = (HOST, PORT)

# File paths
KEY_FILE = 'key.key'
CLIENT_FILES_DIR = 'client_files'

# Ensure the client_files directory exists
os.makedirs(CLIENT_FILES_DIR, exist_ok=True)

# -------------------- Encryption Setup -------------------- #
# Must Generate a key 
def load_key():
    """Load the encryption key from the key.key file."""
    if not os.path.exists(KEY_FILE):
        raise FileNotFoundError("Encryption key not found. Ensure 'key.key' exists.")
    else:
        with open(KEY_FILE, 'rb') as key_file:
            key = key_file.read()
    # Validate the key length
    if len(key) != 44:
        raise ValueError("Invalid Fernet key length.")
    return key

# Initialize Fernet cipher
key = load_key()
cipher = Fernet(key)

# -------------------- Encryption Functions -------------------- #

def send_encrypted(message):
    """Encrypt and send a message to the server."""
    encrypted_message = cipher.encrypt(message.encode())
    client.sendall(encrypted_message)

def receive_encrypted():
    """Receive and decrypt a message from the server."""
    encrypted_message = client.recv(BUFSIZE)
    try:
        decrypted_message = cipher.decrypt(encrypted_message).decode()
    except:
        decrypted_message = ""
    return decrypted_message

# -------------------- File Transfer Functions -------------------- #

def upload_file():
    server_message = receive_encrypted()
    print(server_message)
    filename = input()
    send_encrypted(filename)
    server_message = receive_encrypted()
    print(server_message)
    filepath = os.path.join(CLIENT_FILES_DIR, filename)
    if not os.path.exists(filepath):
        print("File does not exist.")
        send_encrypted("cancel")
        return
    send_encrypted("ready")
    # Read and encrypt the file data
    with open(filepath, 'rb') as f:
        file_data = f.read()
    encrypted_data = cipher.encrypt(file_data)
    # Send the length of the encrypted data
    data_length = len(encrypted_data)
    client.sendall(str(data_length).encode())
    ack = client.recv(BUFSIZE)  # Wait for acknowledgment
    # Send the encrypted data
    client.sendall(encrypted_data)
    # Receive server confirmation
    server_message = receive_encrypted()
    print(server_message)

def download_file():
    server_message = receive_encrypted()
    print(server_message)
    server_message = receive_encrypted()
    print(server_message)
    filename = input()
    send_encrypted(filename)
    server_message = receive_encrypted()
    print(server_message)
    if "File not found" in server_message:
        return
    # Receive the length of the encrypted data
    data_length_str = client.recv(BUFSIZE).decode()
    client.send(b'ACK')  # Send acknowledgment
    try:
        data_length = int(data_length_str)
    except ValueError:
        print("Failed to receive file size.")
        return
    # Receive the encrypted data
    encrypted_data = b''
    while len(encrypted_data) < data_length:
        chunk = client.recv(BUFSIZE)
        if not chunk:
            break
        encrypted_data += chunk
    client.send(b'ACK')  # Send acknowledgment
    try:
        file_data = cipher.decrypt(encrypted_data)
    except:
        print("Failed to decrypt file data.")
        return
    # Save the file data to a file
    filepath = os.path.join(CLIENT_FILES_DIR, filename)
    with open(filepath, 'wb') as f:
        f.write(file_data)
    server_message = receive_encrypted()
    print(server_message)

def file_transfer():
    while True:
        server_message = receive_encrypted()
        print(server_message)
        if "Enter" in server_message or "Do you want" in server_message:
            user_input = input()
            send_encrypted(user_input)
            if user_input == '1':
                upload_file()
            elif user_input == '2':
                download_file()
            elif user_input.lower() == 'exit':
                break
        else:
            print(server_message)

# -------------------- Authentication Functions -------------------- #

def authenticate():
    authenticated = False
    while not authenticated:
        server_message = receive_encrypted()
        print(server_message)
        if "Enter" in server_message or "Do you want" in server_message:
            user_input = input()
            send_encrypted(user_input)
        else:
            print(server_message)
            if "successful" in server_message:
                authenticated = True

# -------------------- Main Client Logic -------------------- #

def main():
    global client
    client = socket.socket()
    client.connect(ADDRESS)
    print("Connected to server at {}:{}".format(HOST, PORT))
    authenticate()
    file_transfer()
    client.close()

if __name__ == "__main__":
    main()
