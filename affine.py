def affine_encrypt(text, a, b):
    """
    Encrypts the given text using an affine cipher with keys 'a' and 'b'.
    :param text: The input text to be encrypted.
    :param a: The multiplicative key (must be coprime with the length of the alphabet).
    :param b: The additive key.
    :return: The encrypted text.
    """
    result = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Convert to uppercase to simplify the encryption process
            char = char.upper()
            # Encrypt the character and add it to the result
            result += chr(((a * (ord(char) - ord('A')) + b) % 26) + ord('A'))
        else:
            # If the character is not a letter, add it as it is
            result += char
    return result

def affine_decrypt(ciphertext, a, b):
    """
    Decrypts the given ciphertext encrypted using an affine cipher with keys 'a' and 'b'.
    :param ciphertext: The encrypted text to be decrypted.
    :param a: The multiplicative key (must be coprime with the length of the alphabet).
    :param b: The additive key.
    :return: The decrypted text.
    """
    result = ""
    # Find the modular inverse of 'a' modulo 26
    a_inv = pow(a, -1, 26)
    for char in ciphertext:
        if char.isalpha():  # Check if the character is a letter
            # Convert to uppercase to simplify the decryption process
            char = char.upper()
            # Decrypt the character and add it to the result
            result += chr(((a_inv * (ord(char) - ord('A') - b)) % 26) + ord('A'))
        else:
            # If the character is not a letter, add it as it is
            result += char
    return result

# Example usage
a = 5  # Multiplicative key (must be coprime with 26)
b = 8  # Additive key
original_text = "Affine Cipher"
encrypted_text = affine_encrypt(original_text, a, b)
decrypted_text = affine_decrypt(encrypted_text, a, b)

print(f"Original text: {original_text}")
print(f"Encrypted text: {encrypted_text}")
print(f"Decrypted text: {decrypted_text}")
