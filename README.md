1️ Project Overview
This project is a desktop application built in Python that enables users to securely encrypt and decrypt files using a password, through a graphical user interface (GUI) created with PyQt5.

It uses AES (Advanced Encryption Standard), one of the most trusted and widely used symmetric encryption algorithms in the world.

2️ Why This Project Matters
 Real-World Use Cases:
Encrypting sensitive documents like contracts, legal records, financial data.

Secure file sharing, especially in remote or cloud-based environments.

Basic personal security: protecting your files on shared or public systems.

 Security Motivation:
Plain files can be easily opened or stolen.

Encryption transforms readable data into ciphertext — unreadable without the correct password/key.

AES offers strong protection, even against advanced attacks.

3️ Core Components of the Project
 A. Cryptographic Logic (in crypto_utlis.py)
 AES Encryption Process:
Password Input: The user provides a password.

Salt Generation: A random 16-byte salt is generated. Salt prevents the same password from producing the same key.

Key Derivation with PBKDF2:

PBKDF2 (Password-Based Key Derivation Function 2) uses the password + salt to derive a strong encryption key.

This slows down brute-force attacks.

AES Algorithm:

Operates in CBC (Cipher Block Chaining) mode.

Requires a random Initialization Vector (IV) (also 16 bytes).

Padding: Data is padded to match AES’s block size (128-bit or 16 bytes).

Encryption: The plaintext file content is encrypted with the AES key.

Output Format: Final encrypted data = salt + iv + ciphertext.

  AES Decryption Process:
Extract salt, iv, and ciphertext from the encrypted file.

Re-derive the AES key from the password and salt using PBKDF2.

Decrypt ciphertext using AES + IV.

Remove padding and return the original plaintext.

 B. GUI Interface (in encrptor_gui.py)
GUI Elements:
Password field: To enter encryption/decryption key.

Encrypt Button: Opens file dialog → encrypts the selected file.

Decrypt Button: Opens file dialog → decrypts selected .aes file.

Quit Button: Exits the app.

Background Image: Enhances visual appeal via CSS in setStyleSheet().

Workflow:
User enters a password.

Chooses a file through a dialog.

Clicks either Encrypt or Decrypt.

Receives success or error message.
