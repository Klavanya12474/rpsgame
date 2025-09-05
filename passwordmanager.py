from cryptography.fernet import Fernet
import os

# Generate and store a new key if it doesn't exist
def load_or_create_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        print("Encryption key generated and saved to 'key.key'.")
    with open("key.key", "rb") as file:
        return file.read()

key = load_or_create_key()
fer = Fernet(key)

def view():
    if not os.path.exists("passwords.txt"):
        print("No saved passwords yet.")
        return

    with open("passwords.txt", "r") as f:
        for line in f:
            data = line.strip()
            if "|" in data:
                try:
                    user, encrypted_pwd = data.split("|")
                    decrypted_pwd = fer.decrypt(encrypted_pwd.encode()).decode()
                    print(f"User: {user} | Password: {decrypted_pwd}")
                except Exception as e:
                    print(f"Error decrypting password for {user}: {e}")
            else:
                print("Skipping malformed line.")

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    encrypted_pwd = fer.encrypt(pwd.encode()).decode()

    with open("passwords.txt", "a") as f:
        f.write(f"{name}|{encrypted_pwd}\n")
    print(f"Password for '{name}' saved successfully.")

def main():
    while True:
        mode = input(
            "\nWould you like to add a new password or view existing ones? (view, add), press 'q' to quit: "
        ).lower()

        if mode == "q":
            print("Exiting password manager.")
            break
        elif mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid mode. Please choose 'view', 'add', or 'q'.")

if __name__ == "__main__":
    main()
