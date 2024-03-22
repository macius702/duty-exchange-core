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
            users = json.load(file)
    except FileNotFoundError:
        users = []
    return users

def save_users(users):
    """Save the user data to the JSON file."""
    with open(USER_FILE, 'w') as file:
        json.dump(users, file)

def save_user(username):
    """Save a new user to the JSON file."""
    users = load_users()
    if username not in [user['username'] for user in users]:
        users.append({'username': username, 'hospitals': []})
        save_users(users)
        return True
    else:
        return False

def login_user(username):
    """Simulate user login by setting the current session."""
    global current_user
    users = load_users()
    if username in [user['username'] for user in users]:
        current_user = username
        return True
    else:
        return False

def add_hospital_to_user(hospital_name):
    """Add a hospital to the current user's profile."""
    users = load_users()
    for user in users:
        if user['username'] == current_user:
            user['hospitals'].append(hospital_name)
            break
    save_users(users)

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
        print("4. User Profile")
        print("5. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            username = input("Enter username: ")
            if login_user(username):
                print(f"Logged in as {username}.")
            else:
                print("Error: Username does not exist. Please register first.")
        elif choice == '2':
            register_page()
        elif choice == '3':
            list_users_page()
        elif choice == '4':
            if current_user:
                user_profile_page()
            else:
                print("Please login to view your profile.")
        elif choice == '5':
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
            print(user['username'])
    else:
        print("No users registered yet.")

def user_profile_page():
    print(f"\nUser Profile: {current_user}")
    action = input("Would you like to add a hospital? (yes/no): ")
    if action.lower() == 'yes':
        hospital_name = input("Enter the name of the hospital: ")
        add_hospital_to_user(hospital_name)
        print(f"{hospital_name} added to your profile.")
    else:
        print("Returning to main menu.")

if __name__ == "__main__":
    main_menu()
