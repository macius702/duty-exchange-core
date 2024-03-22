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



import unittest
from actions import register_user, login_user, add_hospital_to_user, load_users, save_users, current_user  # Adjust imports as needed

class TestHospitalAddition(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up a clean test environment."""
        cls.original_users = load_users()
        save_users([])  # Clear users for testing

    @classmethod
    def tearDownClass(cls):
        """Restore the original test environment."""
        save_users(cls.original_users)

    def setUp(self):
        """Register and log in a user for each test."""
        self.test_username = "testuser_hospital"
        successful_registration = register_user(self.test_username)
        successful_login = login_user(self.test_username)
        if not successful_registration or not successful_login:
            self.fail("Setup failed: could not register or log in test user.")

    def test_add_hospital_to_user(self):
        """Test adding a hospital to the logged-in user's profile."""
        hospital_name = "Test Hospital"
        # Assuming current_user is the logged-in user's username
        add_hospital_to_user(hospital_name)
        users = load_users()

        # Find the logged-in test user and their hospitals
        test_user = next((user for user in users if user['username'] == actions.current_user), None)
        self.assertIsNotNone(test_user, "Logged-in test user not found.")
        
        # Check if the hospital was added
        hospital_names = [hospital['name'] for hospital in test_user['hospitals']]
        self.assertIn(hospital_name, hospital_names, "Hospital was not added to the user.")



from actions import register_user, login_user, add_hospital_to_user, add_ward_to_hospital, load_users, save_users

class TestWardAddition(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up a clean test environment."""
        cls.original_users = load_users()
        save_users([])  # Clear users for testing

    @classmethod
    def tearDownClass(cls):
        """Restore the original test environment."""
        save_users(cls.original_users)

    def setUp(self):
        """Prepare a user, hospital, and ward for each test."""
        self.test_username = "testuser_ward"
        successful_registration = register_user(self.test_username)
        successful_login = login_user(self.test_username)
        self.test_hospital_name = "Test Hospital"
        add_hospital_to_user(self.test_hospital_name)
        if not successful_registration or not successful_login:
            self.fail("Setup failed: could not register or log in test user.")

    def test_add_ward_to_hospital(self):
        """Test adding a ward to a hospital in the user's profile."""
        ward_name = "Test Ward"
        add_ward_to_hospital(self.test_hospital_name, ward_name)
        users = load_users()

        # Find the logged-in test user
        test_user = next((user for user in users if user['username'] == actions.current_user), None)
        self.assertIsNotNone(test_user, "Logged-in test user not found.")

        # Locate the test hospital and verify the ward was added
        test_hospital = next((hospital for hospital in test_user['hospitals'] if hospital['name'] == self.test_hospital_name), None)
        self.assertIsNotNone(test_hospital, "Test hospital not found in user profile.")

        # Check if the ward was added
        self.assertIn(ward_name, test_hospital['wards'], "Ward was not added to the hospital.")

if __name__ == '__main__':
    unittest.main()
