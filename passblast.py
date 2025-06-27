import os
import random
import string
from datetime import datetime

# Color
NEON_BLUE = "\033[96m"
RESET = "\033[0m"

# Banner
banner = f"""
{NEON_BLUE}
$$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\         $$$$$$$\  $$\        $$$$$$\   $$$$$$\ $$$$$$$$\ 
$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\        $$  __$$\ $$ |      $$  __$$\ $$  __$$\\__$$  __|
$$ |  $$ |$$ /  $$ |$$ /  \__|$$ /  \__|       $$ |  $$ |$$ |      $$ /  $$ |$$ /  \__|  $$ |   
$$$$$$$  |$$$$$$$$ |\$$$$$$\  \$$$$$$\ $$$$$$\ $$$$$$$\ |$$ |      $$$$$$$$ |\$$$$$$\    $$ |   
$$  ____/ $$  __$$ | \____$$\  \____$$\\______| $$  __$$\ $$ |      $$  __$$ | \____$$\   $$ |   
$$ |      $$ |  $$ |$$\   $$ |$$\   $$ |       $$ |  $$ |$$ |      $$ |  $$ |$$\   $$ |  $$ |   
$$ |      $$ |  $$ |\$$$$$$  |\$$$$$$  |       $$$$$$$  |$$$$$$$$\ $$ |  $$ |\$$$$$$  |  $$ |   
\__|      \__|  \__| \______/  \______/        \_______/ \________|\__|  \__| \______/   \__|   

{RESET}Version 1.0 | Created By Aashish_Cyber_H4CKS
"""

# Folder for wordlists
WORDLIST_DIR = "Wordlists"
os.makedirs(WORDLIST_DIR, exist_ok=True)

def random_wordlist():
    filename = os.path.join(WORDLIST_DIR, f"random_wordlist_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    print("\n[+] Generating Random Passwords. Press CTRL+C to stop and save.\n")
    try:
        with open(filename, 'w') as f:
            while True:
                length = random.randint(8, 16)
                pwd = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
                print(pwd)
                f.write(pwd + '\n')
    except KeyboardInterrupt:
        print(f"\n[✓] Wordlist saved to: {filename}\n")

def custom_wordlist():
    print("\n[+] Enter the details below:")
    first = input("First Name: ")
    last = input("Last Name: ")
    dob = input("Date of Birth (DDMMYYYY): ")
    nick = input("Nickname: ")
    partner = input("Partner Name: ")
    mother = input("Mother Name: ")
    father = input("Father Name: ")
    pet = input("Pet Name: ")
    extras = input("Any extra words (comma separated): ").split(',')

    words = [first, last, dob, nick, partner, mother, father, pet] + extras
    words = [w.strip() for w in words if w.strip()]

    filename = os.path.join(WORDLIST_DIR, f"custom_wordlist_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    print("\n[+] Generating Custom Wordlist. Press CTRL+C to stop and save.\n")

    try:
        with open(filename, 'w') as f:
            while True:
                combo = random.choices(words, k=random.randint(2, 4))
                pwd = ''.join(combo)
                print(pwd)
                f.write(pwd + '\n')
    except KeyboardInterrupt:
        print(f"\n[✓] Wordlist saved to: {filename}\n")

# Main logic
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    print("[1] Random Wordlist Generator")
    print("[2] Custom Wordlist Generator")
    choice = input("\nChoose an option (1 or 2): ")

    if choice == '1':
        random_wordlist()
    elif choice == '2':
        custom_wordlist()
    else:
        print("[!] Invalid option. Exiting...")
