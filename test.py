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



from actions import register_user, login_user, load_users, save_users  # Adjust import as necessary
import actions

class TestUserLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up for testing."""
        cls.original_users = load_users()  # Save the current state to restore later
        save_users([])  # Start with a clean slate

    @classmethod
    def tearDownClass(cls):
        """Clean up after testing."""
        save_users(cls.original_users)  # Restore the original users

    def setUp(self):
        
        actions.current_user = None  # Ensure current_user is None at the start of each test

    def test_login_sets_current_user(self):
        """Test that a successful login sets the current_user."""
        
        username = "testuser"
        register_user(username)
        self.assertTrue(login_user(username))
        self.assertEqual(actions.current_user, username)

    def test_login_failure_does_not_set_current_user(self):
        """Test that a failed login attempt does not alter current_user."""
        global current_user
        self.assertFalse(login_user("nonexistent_user"))
        self.assertIsNone(actions.current_user)

if __name__ == '__main__':
    unittest.main()
