# Crypto Spammer

Crypto Spammer is a project designed to study the behavior of email security tools, allowing file modifications and testing security detection mechanisms.

![image](https://github.com/user-attachments/assets/90275f1d-b986-4265-b922-645a542da85e)

## 📌 Features

- **Rename Files** (`rename_files.py`): Renames files inside the `Files` folder using sequential numbers, making detection by common names more difficult.
- **Cripto Files** (`cripto_files.py`): Encrypts all files in the `Files` folder, changes the extension, and generates a Python script for decryption.
- **Main Menu** (`crypto_spammer.py`): Displays an interactive menu to execute renaming and encryption functionalities.
- **Main Config** (`main.py`): Contains the main project configurations, where you can modify parameters as needed.

## 🚀 How to Use

### 1️⃣ Run the Interactive Menu
Start the main script to access interactive functionalities:
```bash
python crypto_spammer.py
```

You will see a menu with the following options:
- `A` - Run `rename_files.py`
- `B` - Run `cripto_files.py`
- `C` - Run `main.py`
- `D` - Display the program description

### 2️⃣ Run Individual Scripts
If preferred, you can also run the scripts directly:
```bash
python rename_files.py  # Renames files
python cripto_files.py  # Encrypts files
```

## 📂 Project Structure
```
Crypto Spammer/
│── crypto_spammer.py    # Main menu
│── cripto_files.py      # File encryption
│── rename_files.py      # File renaming
│── main.py              # Main configurations
└── Files/               # Folder where files will be processed
```

## 🛠 Technologies Used
- **Python 3.x**
- **Colorama** (for terminal colors)
- **Cryptography** (for file encryption)

## 📜 License
This project is for educational purposes only and should not be used for malicious intent. Use responsibly! 🔒

---
@Ash3rSec - [GitHub](https://github.com/brunnosaid)

