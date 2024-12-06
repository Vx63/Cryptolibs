# Vigenère Cipher Python Library

This Python library provides two functions for **Vigenère cipher** encryption and decryption. The Vigenère cipher is a method of encrypting alphabetic text by using a keyword. Each letter of the plaintext is shifted by a number of positions in the alphabet corresponding to the keyword.

## Functions

### `encrypt_vigenere(plaintext, keyword)`

Encrypts the given plaintext using the Vigenère cipher with the specified keyword.

#### Parameters:
- `plaintext` (str): The text to be encrypted.
- `keyword` (str): The keyword used for encryption. The keyword is repeated if shorter than the plaintext.

#### Returns:
- (str): The encrypted ciphertext.

#### Example:
```python
ciphertext = encrypt_vigenere("Hello, World!", "KEY")
print(ciphertext)  # Output: "Rijvs, Uyvjn!"
```

### `decrypt_vigenere(ciphertext, keyword)`

Decrypts the given ciphertext that was encrypted with the Vigenère cipher using the specified keyword.

#### Parameters:
- `ciphertext` (str): The text to be decrypted.
- `keyword` (str): The keyword used during encryption. It should match the keyword used for encryption.

#### Returns:
- (str): The decrypted plaintext.

#### Example:
```python
decrypted_text = decrypt_vigenere("Rijvs, Uyvjn!", "KEY")
print(decrypted_text)  # Output: "Hello, World!"
```

## Features:
- Supports both uppercase and lowercase letters.
- Non-alphabetic characters (such as spaces, punctuation) remain unchanged during encryption and decryption.
- The keyword can be of any length. If shorter than the plaintext, it will be repeated.
- Handles both positive and negative shifts based on the keyword letters.

## Example Usage

```python
# Define the plaintext and keyword
plaintext = "Hello, World!"
keyword = "KEY"

# Encrypt the message
ciphertext = encrypt_vigenere(plaintext, keyword)
print("Encrypted:", ciphertext)

# Decrypt the message
decrypted_text = decrypt_vigenere(ciphertext, keyword)
print("Decrypted:", decrypted_text)
```

### Output:
```
Encrypted: Rijvs, Uyvjn!
Decrypted: Hello, World!
```

## Installation

No installation is required. You can simply copy and paste the functions into your Python project and use them directly.
