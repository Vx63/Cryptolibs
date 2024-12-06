# Caesar Cipher Library

This Python library implements a simple Caesar Cipher for encryption and decryption. The Caesar Cipher is a classical encryption technique where each letter in the plaintext is shifted by a certain number of positions in the alphabet. This library provides two functions:

- `encryptcaesar(plaintext, shift_key)`: Encrypts the given plaintext using the Caesar Cipher with the specified shift key.
- `decryptcaesar(ciphertext, shift_key)`: Decrypts the given ciphertext using the Caesar Cipher with the specified shift key.

## Functions

### `encryptcaesar(plaintext, shift_key)`

Encrypts the given plaintext using a Caesar Cipher with the specified shift key.

#### Parameters:
- `plaintext` (str): The text to be encrypted.
- `shift_key` (int): The number of positions each letter in the plaintext is shifted. Can be positive or negative.

#### Returns:
- (str): The encrypted ciphertext.

#### Example:
```python
encrypted = encryptcaesar("Hello, World!", 3)
print(encrypted)  # "Khoor, Zruog!"
```

### `decryptcaesar(ciphertext, shift_key)`

Decrypts the given ciphertext that was encrypted with the Caesar Cipher and a specified shift key.

#### Parameters:
- `ciphertext` (str): The text to be decrypted.
- `shift_key` (int): The number of positions each letter in the ciphertext is shifted. Must match the shift key used during encryption.

#### Returns:
- (str): The decrypted plaintext.

#### Example:
```python
decrypted = decryptcaesar("Khoor, Zruog!", 3)
print(decrypted)  # "Hello, World!"
```

## Features:
- Supports both uppercase and lowercase letters.
- Non-alphabetic characters (such as spaces, punctuation) are not affected by the cipher and remain unchanged.
- Handles both positive and negative shift keys.

## Example Usage

```python
# Encryption
plaintext = "Hello, World!"
shift_key = 3
ciphertext = encryptcaesar(plaintext, shift_key)
print("Encrypted:", ciphertext)

# Decryption
decrypted_text = decryptcaesar(ciphertext, shift_key)
print("Decrypted:", decrypted_text)
```

Output:
```
Encrypted: Khoor, Zruog!
Decrypted: Hello, World!
```

## Installation

No installation is required. Simply download or copy the code into your Python project and import the functions.
