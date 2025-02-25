import os
import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def display_banner():
    banner = f'''
{Fore.BLUE}       db                    88            ad888888b,                                                                                                                           
{Fore.LIGHTBLUE_EX}      d88b                   88           d8#     #88                                                                                                                           
{Fore.CYAN}     d8'`8b                  88                   a8P                                                                                                                           
{Fore.LIGHTCYAN_EX}    d8'  `8b      ,adPPYba,  88,dPPYba,        aad8#   8b,dPPYba,                                                                                                               
{Fore.BLUE}   d8YaaaaY8b     I8[    ##  88P'    #8a       ##Y8,   88P'   #Y8                                                                                                               
{Fore.LIGHTBLUE_EX}  d8########8b     #"Y8ba,   88       88          #8b  88                                                                                                                       
{Fore.CYAN} d8'        `8b   aa    ]8I  88       88  Y8,     a88  88                                                                                                                       
{Fore.LIGHTCYAN_EX}d8'          `8b  #"YbbdP"'  88       88   "Y888888P'  88                                                                                                                       

{Fore.BLUE}  ,ad8888ba,                                                              ad88888ba                                                                                            
{Fore.LIGHTBLUE_EX} d8"'    `"8b                                         ,d                 d8"     "8b                                                                                            
{Fore.CYAN}d8'                                                   88                 Y8,                                                                                                   
{Fore.LIGHTCYAN_EX}88             8b,dPPYba,  8b       d8  8b,dPPYba,  MM88MMM  ,adPPYba,   `Y8aaaaa,    8b,dPPYba,   ,adPPYYba,  88,dPYba,,adPYba,   88,dPYba,,adPYba,    ,adPPYba,  8b,dPPYba,  
{Fore.BLUE}88             88P'   "Y8  `8b     d8'  88P'    "8a   88    a8"     "8a    `#####8b,  88P'    "8a  ""     `Y8  88P'   "88"    "8a  88P'   "88"    "8a  a8P#####88  88P'   "Y8  
{Fore.LIGHTBLUE_EX}Y8,            88           `8b   d8'   88       d8   88    8b       d8          `8b  88       d8  ,adPPPPP88  88      88      88  88      88      88  8PP#####"""  88          
{Fore.CYAN} Y8a.    .a8P  88            `8b,d8'    88b,   ,a8"   88,   "8a,   ,a8"  Y8a     a8P  88b,   ,a8"  88,    ,88  88      88      88  88      88      88  "8b,   ,aa  88          
{Fore.LIGHTCYAN_EX}  `"Y8888Y"'   88              Y88'     88`YbbdP"'    "Y888  `"YbbdP"'    "Y88888P"   88`YbbdP"'   `"8bbdP"Y8  88      88      88  88      88      88   `"Ybbd8"'  88          
{Fore.BLUE}                               d8'      88                                            88                                                                                       
{Fore.LIGHTBLUE_EX}                              d8'       88                                            88                                                                                        

{Fore.RED}@Ash3rSec - github.com/brunnosaid{Style.RESET_ALL}
'''
    print(banner)


def display_description():
    description = """
CryptoSpammer is a project designed to study the behavior of Email Security tools.
Use it as follows:
    1. Modify the configuration data in main.py
    2. If necessary, modify the configuration data in cripto_files.py

[Rename Files]
Renames files in the "Files" folder to sequential numbers, avoiding detection by common names.

[Cripto Files]
Encrypts all contents in the "Files" folder, changing the extension and encrypting them with a customizable password (default: ash3r). It compresses the file and generates a Python script for decryption.
"""
    print(description)


def show_menu():
    print("\nChoose an option:")
    print("A - Run rename_files.py")
    print("B - Run cripto_files.py")
    print("C - Run main.py")
    print("D - Access program description")
    choice = input("Enter your choice: ").strip().upper()
    return choice


def main():
    display_banner()
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        display_description()
        return

    while True:
        option = show_menu()
        if option == "A":
            os.system("python rename_files.py")
        elif option == "B":
            os.system("python cripto_files.py")
        elif option == "C":
            os.system("python main.py")
        elif option == "D":
            display_description()
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
