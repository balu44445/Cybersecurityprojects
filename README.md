
# 🔐 AES File Encryptor/Decryptor with PyQt5

## 1️⃣ Project Overview

This desktop application is built with **Python** and **PyQt5**, allowing users to securely **encrypt and decrypt files** using a password. It employs **AES (Advanced Encryption Standard)**, one of the most trusted symmetric encryption algorithms globally.

> 💡 Users interact through a simple and clean **Graphical User Interface (GUI)** to process files without needing cryptographic knowledge.

---

## 2️⃣ Why This Project Matters

### ✅ Real-World Use Cases

* Encrypting sensitive documents: contracts, legal records, finance reports.
* Secure file sharing via email or cloud platforms.
* Personal data protection on shared or public computers.

### 🔒 Security Motivation

* Unprotected files are easily exposed, copied, or modified.
* Encryption transforms readable data into **ciphertext**, unintelligible without the correct **key**.
* **AES** is widely used in industry (e.g., by governments, enterprises) for secure data handling.

---

## 3️⃣ Core Components

### 🧠 A. Cryptographic Logic (`crypto_utlis.py`)

#### 🔐 AES Encryption Process

* **Password Input**: User provides a password.
* **Salt Generation**: A random 16-byte salt is created to ensure unique keys.
* **Key Derivation**: Uses **PBKDF2** (Password-Based Key Derivation Function 2) to convert password + salt into a strong 256-bit AES key.
* **Initialization Vector (IV)**: Random 16-byte IV for AES-CBC mode.
* **Padding**: File content is padded to 16-byte blocks.
* **Encryption**: File data is encrypted.
* **Output**: Encrypted file = `salt + iv + ciphertext`.

#### 🔓 AES Decryption Process

* Extract `salt`, `iv`, and `ciphertext` from the file.
* Derive the AES key using the same password and salt.
* Decrypt using AES-CBC.
* Unpad the decrypted data to retrieve the original file content.

---

### 💻 B. Graphical User Interface (`encrptor_gui.py`)

#### GUI Elements:

* **QLineEdit**: Secure password entry.
* **QPushButton**:

  * `Encrypt File`: Select and encrypt a file.
  * `Decrypt File`: Select and decrypt a `.aes` file.
  * `Quit`: Close the application.

#### 🧭 Workflow:

1. User enters a **password**.
2. Chooses a file via **File Dialog**.
3. Clicks **Encrypt** or **Decrypt**.
4. Receives a **Success** or **Error** message box.

---

## 🖼️ Optional Features

* **Background Image**: A static image can be added to the GUI for visual appeal.
* **Error Handling**: Invalid files or incorrect passwords are gracefully handled.
* **Output Naming**:

  * Encrypted files: `filename.aes`
  * Decrypted files: `filename.dec`

---

## ✅ How to Run

```bash
# 1. Navigate to the project directory
cd path/to/Encryption

# 2. Activate virtual environment (if used)
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# 3. Run the application
python encrptor_gui.py
```

> 🔍 Make sure `PyQt5` and `cryptography` are installed (`pip install pyqt5 cryptography`).

