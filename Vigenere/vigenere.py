def encrypt_vigenere(plaintext, keyword):
    ciphertext = []
    keyword = keyword.lower()  # Ensure the keyword is in lowercase
    keyword_repeated = [keyword[i % len(keyword)] for i in range(len(plaintext))]  # Repeat keyword as necessary

    for p, k in zip(plaintext, keyword_repeated):
        if p.isalpha():  # Encrypt only alphabetic characters
            shift = ord(k) - ord('a')  # Shift based on the letter in the keyword
            if p.islower():
                # Encrypt lowercase letters
                new_char = chr((ord(p) - ord('a') + shift) % 26 + ord('a'))
            elif p.isupper():
                # Encrypt uppercase letters
                new_char = chr((ord(p) - ord('A') + shift) % 26 + ord('A'))
            ciphertext.append(new_char)
        else:
            # Non-alphabetic characters remain unchanged
            ciphertext.append(p)

    return ''.join(ciphertext)

def decrypt_vigenere(ciphertext, keyword):
    plaintext = []
    keyword = keyword.lower()  # Ensure the keyword is in lowercase
    keyword_repeated = [keyword[i % len(keyword)] for i in range(len(ciphertext))]  # Repeat keyword as necessary

    for c, k in zip(ciphertext, keyword_repeated):
        if c.isalpha():  # Decrypt only alphabetic characters
            shift = ord(k) - ord('a')  # Shift based on the letter in the keyword
            if c.islower():
                # Decrypt lowercase letters
                new_char = chr((ord(c) - ord('a') - shift) % 26 + ord('a'))
            elif c.isupper():
                # Decrypt uppercase letters
                new_char = chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
            plaintext.append(new_char)
        else:
            # Non-alphabetic characters remain unchanged
            plaintext.append(c)

    return ''.join(plaintext)
