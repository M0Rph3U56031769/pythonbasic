import os


class Authentication:

    @staticmethod
    def get_username():
        """
        Gets the username from os and returns it
        """

        user_name = os.getlogin()
        return user_name
