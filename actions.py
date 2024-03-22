import json
import sys

# Path to the JSON file where user data is stored
USER_FILE = 'users.json'

def load_users():
    """Load users from the JSON file."""
    try:
        with open(USER_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_user(username):
    """Save a new user to the JSON file."""
    users = load_users()
    if username not in users:
        users.append(username)  # Store just the username
        with open(USER_FILE, 'w') as file:
            json.dump(users, file)
        return True
    else:
        return False

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Login / View Landing Page")
        print("2. Register")git 
        print("3. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            landing_page()
        elif choice == '2':
            register_page()
        elif choice == '3':
            sys.exit("Thank you for using the app.")
        else:
            print("Invalid choice. Please try again.")

def register_page():
    print("\nRegister Page")
    username = input("Choose a username: ")
    
    if save_user(username):
        print(f"Registration successful. Welcome, {username}!")
    else:
        print("This username already exists. Please try a different one.")

def landing_page():
    print("\nLanding Page")
    users = load_users()
    if users:
        print("List of Users:")
        for user in users:
            print(user)
    else:
        print("No users registered yet.")

if __name__ == "__main__":
    main_menu()
