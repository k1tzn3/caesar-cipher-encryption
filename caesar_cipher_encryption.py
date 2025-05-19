
def encrypt_message(message, shift):
    encrypted_message = ""

    for char in message:
        if char.isalpha():
            # Preserve case
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around the alphabet
            shifted = (ord(char) - base + shift) % 26 + base
            encrypted_message += chr(shifted)
        else:
            # Leave non-alphabet characters unchanged
            encrypted_message += char

    return encrypted_message

# Example usage
message = "Hello, World!"
shift = 3
encrypted = encrypt_message(message, shift)
print("Encrypted message:", encrypted)
