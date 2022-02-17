class User:
    user_list = []  # Created an empty user list

    def __init__(self, username, password, email):
        """
        The __init__ method defines properties of the object
         :param username:
        :param password:
        :param email:
        """
        self.username = username
        self.password = password
        self.email = email

    def save_user(self):
        """
        Method to add a new user to the user list
        :return:
        """
        User.user_list.append(self)

    def delete_user(self):
        """
        Method to delete user from the user list
        :return:
        """
        User.user_list.remove(self)

    @classmethod
    def find_user_by_username(cls, username):
        """
        Method that returns user details that match the username
        :param username:
        :return:
        """
        for user in cls.user_list:
            if user.username == username:
                return user

    @classmethod
    def user_exists(cls, username, password):
        """
        Method to check if a user exists
        :param password:
        :param username:
        :return:
        """
        for user in cls.user_list:
            if user.username == username and user.password == password:
                return True

        return False

    @classmethod
    def display_users(cls):
        """
        Method that returns a list of all users
        :return:
        """
        return cls.user_list
