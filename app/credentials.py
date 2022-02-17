import random
import string


class Credential:
    credential_list = []  # Created an empty credential list

    def __init__(self, social_media, account, password):
        """
        The init method defines the properties of the object
        :param social_media:
        :param account:
        :param password:
        """
        self.social = social_media
        self.account = account
        self.password = password

    def save_credential(self):
        """
        Saving the user credentials
        :return:
        """
        Credential.credential_list.append(self)

    def delete_credential(self):
        """
        Deleting the user credentials
        :return:
        """
        Credential.credential_list.remove(self)

    @classmethod
    def display_credentials(cls):
        """
        Function to display credentials
        :return:
        """
        return cls.credential_list

    def automatic_generated_password(length=12, password=string.digits + string.ascii_letters + string.ascii_uppercase):
        """
        Function to generate a random password
        :param password:
        :return:
        """

        random_password = ''.join(random.choice(password) for i in range(length))
        return random_password
