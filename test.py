import unittest
from actions import register_user, load_users  # Adjust import as necessary

class TestUserRegistration(unittest.TestCase):
    def test_user_registration(self):
        # Ensure the environment is clean (no users with this name)
        # Caution: This will clear your current data!
        test_username = "testuser"
        register_user(test_username)  # Attempt to register a test user
        users = load_users()  # Load the list of all users
        registered_usernames = [user['username'] for user in users]
        self.assertIn(test_username, registered_usernames)  # Check if the test user is in the list

if __name__ == '__main__':
    unittest.main()
