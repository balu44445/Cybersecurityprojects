import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QMessageBox, QLabel, QLineEdit
)
from crypto_utlis import encrypt, decrypt

class EncryptorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Secure AES File Encryptor/Decryptor')
        self.setGeometry(100, 100, 350, 250)

        layout = QVBoxLayout()

        self.label = QLabel("Enter password:")
        layout.addWidget(self.label)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.encrypt_btn = QPushButton('Encrypt File')
        self.encrypt_btn.clicked.connect(self.encrypt_file)
        layout.addWidget(self.encrypt_btn)

        self.decrypt_btn = QPushButton('Decrypt File')
        self.decrypt_btn.clicked.connect(self.decrypt_file)
        layout.addWidget(self.decrypt_btn)

        self.quit_btn = QPushButton('Quit')
        self.quit_btn.clicked.connect(self.close)
        layout.addWidget(self.quit_btn)

        self.setLayout(layout)

    def encrypt_file(self):
        self.process_file('encrypt')

    def decrypt_file(self):
        self.process_file('decrypt')

    def process_file(self, mode):
        password = self.password_input.text()
        if not password:
            QMessageBox.warning(self, "Error", "Password cannot be empty.")
            return

        filepath, _ = QFileDialog.getOpenFileName(self, "Select File")
        if not filepath:
            return

        try:
            with open(filepath, 'rb') as f:
                data = f.read()

            if mode == 'encrypt':
                result = encrypt(data, password)
                out_path = filepath + '.aes'
            else:
                result = decrypt(data, password)
                out_path = filepath.replace('.aes', '') + '.dec'

            with open(out_path, 'wb') as f:
                f.write(result)

            QMessageBox.information(self, "Success", f"File {mode}ed:\n{out_path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to {mode} file:\n{str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EncryptorApp()
    window.show()
    sys.exit(app.exec_())
