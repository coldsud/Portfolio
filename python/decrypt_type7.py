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
