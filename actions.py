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

def register_user(username):
    """Attempt to register a new user."""
    users = load_users()
    if username not in [user['username'] for user in users]:
        users.append({'username': username, 'hospitals': []})
        save_users(users)
        return True  # Indicates the user was successfully registered
    else:
        return False  # Indicates the user already exists

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
            # Ensure hospital is now an object with a name and wards
            user['hospitals'].append({'name': hospital_name, 'wards': []})
            break
    save_users(users)

def add_ward_to_hospital(hospital_name, ward_name):
    """Add a ward to a specific hospital for the current user."""
    users = load_users()
    for user in users:
        if user['username'] == current_user:
            for hospital in user['hospitals']:
                if hospital['name'] == hospital_name:
                    hospital['wards'].append(ward_name)
                    break
    save_users(users)


def add_hospital_to_user(hospital_name):
    """Add a hospital (as an object) to the current user's profile."""
    users = load_users()
    for user in users:
        if user['username'] == current_user:
            # Ensure hospital is added as an object with 'name' and 'wards'
            new_hospital = {'name': hospital_name, 'wards': []}
            user['hospitals'].append(new_hospital)
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

    registration_success = register_user('new_username')
    if registration_success:
        print("User registered successfully.")
    else:
        print("User already exists.")


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
    users = load_users()
    current_user_hospitals = []
    for user in users:
        if user['username'] == current_user:
            current_user_hospitals = user['hospitals']
            break
    
    if current_user_hospitals:
        print("Your Hospitals and Wards:")
        for hospital in current_user_hospitals:
            print(f"- {hospital['name']}")
            for ward in hospital['wards']:
                print(f"    - Ward: {ward}")
    else:
        print("You have no hospitals listed in your profile.")
    
    action = input("Would you like to add a hospital or ward? (hospital/ward/no): ")
    if action.lower() == 'hospital':
        hospital_name = input("Enter the name of the hospital: ")
        add_hospital_to_user(hospital_name)
        print(f"{hospital_name} added to your profile.")
    elif action.lower() == 'ward':
        hospital_name = input("Enter the name of the hospital to add a ward to: ")
        ward_name = input("Enter the name of the ward: ")
        add_ward_to_hospital(hospital_name, ward_name)
        print(f"Ward {ward_name} added to hospital {hospital_name}.")
    else:
        print("Returning to main menu.")


if __name__ == "__main__":
    main_menu()
