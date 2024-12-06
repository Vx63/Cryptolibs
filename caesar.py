def encryptcaesar(plaintext, shift_key):
    ciphertext = ""

    for char in plaintext:
        if char.isupper():
            char_index = ord(char) - ord("A")
            char_shifted = (char_index + shift_key) % 26 + ord("A")

            char_encrypted = chr(char_shifted)

            ciphertext +=char_encrypted

        elif char.islower():
            char_index = ord(char) - ord("a")
            char_shifted = (char_index + shift_key) % 26 + ord("a")

            char_encrypted = chr(char_shifted)

            ciphertext +=char_encrypted

        else:
            ciphertext +=char

    return ciphertext

def decryptcaesar(ciphertext,shift_key):
    dec_plaintext= ""

    for char in ciphertext:
        if char.isupper():
            char_index = ord(char) - ord("A")
            char_unshifted = (char_index - shift_key) % 26 + ord("A")

            char_decrypted = chr(char_unshifted)

            dec_plaintext +=char_decrypted

        elif char.islower():
            char_index = ord(char) - ord("a")
            char_unshifted = (char_index - shift_key) % 26 + ord("a")

            char_decrypted = chr(char_unshifted)

            dec_plaintext +=char_decrypted

        else:
            dec_plaintext +=char

    return dec_plaintext
