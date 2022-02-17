import unittest
from user import User


class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the User contact class behaviours
    """

    def setUp(self) -> None:
        """
        Set up method to run before each test cases.
        :return:
        """
        self.new_user = User("Sam", "Tests123", "samdevtests@gmail.com")  # create contact object

    def test_init(self):
        """
        test_init test case tests if the objects are being initiated correctly
        :return:
        """
        self.assertEqual(self.new_user.username, "Sam")
        self.assertEqual(self.new_user.password, "Tests123")
        self.assertEqual(self.new_user.email, "samdevtests@gmail.com")

    def test_save_user(self):
        """
        test_save_user test case tests if a user is being save correctly
        in the user list
        :return:
        """
        self.new_user.save_user()

        self.assertEqual(len(User.user_list), 1)

    def tearDown(self) -> None:
        """
        tearDown method that does clean up after each test case has run.
        :return:
        """
        User.user_list = []

    def test_save_multiple_users(self):
        """
        test_save_multiple_users test case tests if multiple users can be saved correctly
        in the user list
        :return:
        """
        self.new_user.save_user()
        test_user = User("test_user", "Testuser1", "samdevtests@gmail.com")
        test_user.save_user()

        self.assertEqual(len(User.user_list), 2)

    def test_delete_user(self):
        """
        test_delete_user test case tests if a user can be deleted successfully from the
        user list
        :return:
        """
        self.new_user.save_user()
        test_user = User("test_user", "Testuser1", "samdevtests@gmail.com")
        test_user.save_user()

        test_user.delete_user()

        self.assertEqual(len(User.user_list), 1)

    def test_find_user_by_username(self):
        """
        test_find_user_by_username test case tests if we can find a user by a username
        :return:
        """
        self.new_user.save_user()
        test_user = User("test_user", "Testuser1", "samdevtests@gmail.com")
        test_user.save_user()

        found_user = User.find_user_by_username("test_user")

        self.assertEqual(found_user.email, test_user.email)

    def test_user_exists(self):
        """
        test to check if we can return a Boolean  if we cannot find the user
        :return:
        """
        self.new_user.save_user()
        test_user = User("test_user", "Testuser1", "samdevtests@gmail.com")
        test_user.save_user()

        user_exists = User.user_exists("test_user", "Testuser1")

        self.assertTrue(user_exists)

    def display_all_users(self):
        """
        display_all_users test case returns a list of all saved users
        :return:
        """
        self.assertEqual(User.display_users(), User.user_list)


if __name__ == '__main__':
    unittest.main()
