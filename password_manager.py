import os

def print_banner():
    banner = """ 
\033[38;2;0;100;0m


.▄▄ · ▄▄▄ . ▄▄· ▄• ▄▌▄▄▄  ▄▄▄ .     ▄▄▄· ▄▄▄· .▄▄ · .▄▄ · 
▐█ ▀. ▀▄.▀·▐█ ▌▪█▪██▌▀▄ █·▀▄.▀·    ▐█ ▄█▐█ ▀█ ▐█ ▀. ▐█ ▀. 
▄▀▀▀█▄▐▀▀▪▄██ ▄▄█▌▐█▌▐▀▀▄ ▐▀▀▪▄     ██▀·▄█▀▀█ ▄▀▀▀█▄▄▀▀▀█▄
▐█▄▪▐█▐█▄▄▌▐███▌▐█▄█▌▐█•█▌▐█▄▄▌    ▐█▪·•▐█ ▪▐▌▐█▄▪▐█▐█▄▪▐█
 ▀▀▀▀  ▀▀▀ ·▀▀▀  ▀▀▀ .▀  ▀ ▀▀▀     .▀    ▀  ▀  ▀▀▀▀  ▀▀▀▀ 

\033[0m
    

<<<<<==================================================>>>>>
                        Secure-Pass
        A Command Line Python Based Password Manager 
<<<<<==================================================>>>>>
                 Made by Code-With-Abdul
                       Version 1.0
<<<<<==================================================>>>>>



    """

    print(banner)


PASSWORD_FILE = "passwords.txt"
WEBSITE_FILE = "websites.txt"
MASTER_PASSWORD_FILE = "master_password.txt"

def load_passwords():
    passwords = {}
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, 'r') as f:
            lines = f.readlines()
            for line in lines:
                website, username, password = line.strip().split(',')
                passwords[website] = (username, password)
    return passwords

def save_passwords(passwords):
    with open(PASSWORD_FILE, 'w') as f:
        for website, (username, password) in passwords.items():
            f.write(f"{website},{username},{password}\n")

def load_websites():
    websites = []
    if os.path.exists(WEBSITE_FILE):
        with open(WEBSITE_FILE, 'r') as f:
            websites = [line.strip() for line in f.readlines()]
    return websites

def save_website(website):
    with open(WEBSITE_FILE, 'a') as f:
        f.write(f"{website}\n")

def load_master_password():
    if os.path.exists(MASTER_PASSWORD_FILE):
        with open(MASTER_PASSWORD_FILE, 'r') as f:
            return f.read().strip()
    else:
        return None

def save_master_password(master_password):
    with open(MASTER_PASSWORD_FILE, 'w') as f:
        f.write(master_password)

def authenticate():
    master_password = load_master_password()
    if master_password is None:
        print("No master password set. Set a new master password.")
        set_master_password()
        return True
    else:
        attempts = 3
        while attempts > 0:
            password = input("Enter master password: ")
            if password == master_password:
                return True
            else:
                attempts -= 1
                print(f"Incorrect password. {attempts} attempts left.")
        print("Too many failed attempts. Exiting.")
        return False

def set_master_password():
    master_password = input("Enter a new master password: ")
    confirm_password = input("Confirm master password: ")
    if master_password == confirm_password:
        save_master_password(master_password)
        print("Master password set successfully.")
    else:
        print("Passwords do not match. Please try again.")

def reset_master_password():
    old_master_password = input("Enter old master password: ")
    if old_master_password == load_master_password():
        set_master_password()
    else:
        print("Old master password is incorrect.")

def add_password(passwords, websites):
    website = input("Enter website: ")
    if website not in websites:
        websites.append(website)
        save_website(website)
    username = input("Enter username: ")
    password = input("Enter password: ")
    passwords[website] = (username, password)
    save_passwords(passwords)
    print("Password saved successfully.")

def get_password(passwords):
    websites = load_websites()
    print("List of websites:")
    for i, website in enumerate(websites, 1):
        print(f"{i}. {website}")
    choice = input("Select the website (enter the number): ")
    print("-------------------------------------")
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(websites):
            website = websites[index]
            if website in passwords:
                username, password = passwords[website]
                print(f"Username: {username}")
                print(f"Password: {password}")
            else:
                print("Password not found.")
        else:
            print("Invalid choice.")
    else:
        print("Invalid input.")

def main():
    print_banner()
    if not authenticate():
        return

    passwords = load_passwords()

    while True:
        print("\nMenu:-")
        print("1- Add password")
        print("2- Get password")
        print("3- Reset master password")
        print("4- Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            websites = load_websites()
            add_password(passwords, websites)
        elif choice == '2':
            get_password(passwords)
        elif choice == '3':
            reset_master_password()
        elif choice == '4':
            print("Don't worry all of your Passwords are safe")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
