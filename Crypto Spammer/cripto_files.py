import os
import hashlib
import secrets
import zipfile
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

# Configurations
SOURCE_FOLDER = "../daily"      # Replace with the actual folder path
PASSWORD = "ash3r"              # Choose a secure password
ENCRYPTED_EXTENSION = ".as3"    # Extension for encrypted files


def generate_key(password):
    """Generates a 32-byte key (AES-256) from a password."""
    return hashlib.sha256(password.encode()).digest()


def generate_decryption_script(file_name):
    """Generates a Python script to decrypt the file."""
    script = f'''import os
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def generate_key(password):
    return hashlib.sha256(password.encode()).digest()

def decrypt_file(file, password):
    key = generate_key(password)
    with open(file, "rb") as f:
        iv = f.read(16)
        encrypted_data = f.read()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    decrypted_data = unpadder.update(padded_data) + unpadder.finalize()

    original_name = file.replace("{ENCRYPTED_EXTENSION}", "")
    with open(original_name, "wb") as f:
        f.write(decrypted_data)

    print(f"Decrypted file: {original_name}")

decrypt_file("{file_name}", "{PASSWORD}")
'''
    return script


def encrypt_file(file_path, key):
    """Encrypts a file and generates a ZIP package with a decryption script."""
    iv = secrets.token_bytes(16)
    with open(file_path, "rb") as f:
        data = f.read()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    encrypted_file_name = file_path + ENCRYPTED_EXTENSION
    with open(encrypted_file_name, "wb") as f:
        f.write(iv + encrypted_data)

    print(f"Encrypted file: {encrypted_file_name}")
    os.remove(file_path)
    print(f"Original file removed: {file_path}")

    output_folder = os.path.splitext(file_path)[0]
    os.makedirs(output_folder, exist_ok=True)
    os.rename(encrypted_file_name, os.path.join(output_folder, os.path.basename(encrypted_file_name)))

    script = generate_decryption_script(os.path.basename(encrypted_file_name))
    script_path = os.path.join(output_folder, "decrypt.py")
    with open(script_path, "w") as f:
        f.write(script)

    zip_path = f"{output_folder}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(output_folder):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), output_folder))

    print(f"ZIP package created: {zip_path}")

    for root, _, files in os.walk(output_folder, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        os.rmdir(root)


def process_folder():
    """Encrypts all files in the folder and creates ZIP packages."""
    key = generate_key(PASSWORD)
    for file in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file)
        if os.path.isfile(file_path) and not file.endswith(ENCRYPTED_EXTENSION):
            encrypt_file(file_path, key)


if __name__ == "__main__":
    process_folder()
