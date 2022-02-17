import unittest
from credentials import Credential


class TestCredential(unittest.TestCase):
    """
    Test class that defines test cases for the Credential contact class behaviours
    """

    def setUp(self) -> None:
        """
        Set up method to be run before each test cases
        :return:
        """
        self.new_credentials = Credential("Ubidy", "Sam", "Tests123")

    def test_save_credential(self):
        """
        test_save_credential test case tests if a credential is saved
        correctly in the credential list
        :return:
        """
        self.new_credentials.save_credential()

        self.assertEqual(len(Credential.credential_list), 1)

    def tearDown(self) -> None:
        """
        tearDown method that does clean up after each test case has run.
        :return:
        """
        Credential.credential_list = []

    def test_save_multiple_credentials(self):
        """
                test_save_multiple_credentials test case tests if multiple credentials can be saved correctly
                in the credential list
                :return:
                """
        self.new_credentials.save_credential()
        new_user = Credential("Ardstop", "Ardern", "Tests123")
        new_user.save_credential()

        self.assertEqual(len(Credential.credential_list), 2)

    def test_delete_credential(self):
        """
                test_delete_credential case tests if a credential can be deleted successfully from the
                credential list
                :return:
                """
        self.new_credentials.save_credential()
        new_user = Credential("Westapp", "Sam", "Tests123")
        new_user.save_credential()

        new_user.delete_credential()

        self.assertEqual(len(Credential.credential_list), 1)

    def test_display_user_credentials(self):
        """
        test_display_user_credentials tests if we can display the users details correctly
        :return:
        """
        self.new_credentials.save_credential()
        new_user = Credential("MamaApp", "Hamida", "Tests123")
        new_user.save_credential()

        self.assertEqual(Credential.display_credentials(), Credential.credential_list)


if __name__ == '__main__':
    unittest.main()
