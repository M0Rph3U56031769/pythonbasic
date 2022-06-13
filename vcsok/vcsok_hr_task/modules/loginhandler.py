import os
import json
from typing import Dict


class LoginHandler:
    def __init__(self, json_path: str):
        self.json_path = json_path
        self.users = {}
        self.current_user_name = None
        self.current_user_level = None
        self.load_data()

    def load_data(self) -> None:
        """
        Loads the data of the users from provided path
        """
        if os.path.exists(self.json_path):
            with open(self.json_path, "r", encoding="utf-8") as fp:
                self.users = json.load(fp)

    def write_data(self) -> None:
        """
        Writes the data back to the save file
        """
        with open(self.json_path, "w", encoding="utf-8") as fp:
            json.dump(self.users, fp, indent=4)

    def save_user(self, name: str, level: int) -> None:
        """
        Saves users with name and level
            Parameters:
                name (str): name of user
                level (int): level of user
        """
        self.users[name] = {"user_level": level}
        self.write_data()

    def get_user(self, name: str) -> Dict[str, int]:
        """
        Returns a user with given name
            Parameters:
                name (str)
            Returns:
                (dict): Returns a user with name and user level
        """
        for key, value in self.users.items():
            if key.lower() == name.lower():
                return value
        else:
            return {}

    def set_current_user(self, name: str, level: int):
        """
        Sets the current user
            Parameters:
                name (str): name of user
                level (int): level of user
        """
        self.current_user_name = name
        self.current_user_level = level
