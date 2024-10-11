def simple_encrypt(word, shift):
    # Adjust shift to be within the alphabet range
    shift = shift % 26

    encrypted_word = ""

    # Loop through each character in the word
    for ch in word:
        if 'a' <= ch <= 'z':  # Handle lowercase letters
            new_char = chr(((ord(ch) - ord('a') + shift) % 26) + ord('a'))
        elif 'A' <= ch <= 'Z':  # Handle uppercase letters
            new_char = chr(((ord(ch) - ord('A') + shift) % 26) + ord('A'))
        else:
            new_char = ch  # Keep non-alphabet characters unchanged

        encrypted_word += new_char

    print("Encrypted word:", encrypted_word)
    return

# Get user input
word = input("Enter a word to encrypt: ")
shift = int(input("Enter the distance to shift each letter: "))

# Encrypt the word
simple_encrypt(word, shift)