import json
import sys

# Path to the JSON file where user data is stored
USER_FILE = 'users.json'

# Current user session (None if no user is logged in)
current_user = None

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

def login_user(username):
    """Simulate user login by setting the current session."""
    global current_user
    users = load_users()
    if username in users:
        current_user = username
        return True
    return False

def main_menu():
    global current_user
    while True:
        print("\nMain Menu")
        if current_user:
            print(f"You are logged in as: {current_user}")
        else:
            print("You are not logged in.")
        print("1. Login / Change User")
        print("2. Register")
        print("3. List All Users")
        print("4. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            username = input("Enter username: ")
            if login_user(username):
                print(f"Logged in as {username}.")
            else:
                print("Username does not exist. Please register first.")
        elif choice == '2':
            register_page()
        elif choice == '3':
            list_users_page()
        elif choice == '4':
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

def list_users_page():
    print("\nList of All Users")
    users = load_users()
    if users:
        for user in users:
            print(user)
    else:
        print("No users registered yet.")

if __name__ == "__main__":
    main_menu()
