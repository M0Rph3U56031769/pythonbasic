import os
import pathlib
from .datahandler import DataHandler
from .loginhandler import LoginHandler

USER_LEVEL_DICT = {
    0: "viewer",
    1: "editor"
}

MAIN_MENU_OPTIONS = {
    0: "Exit HR Portal",
    1: "See current employees",
    2: "Search for an employee",
    3: "Add new employee",
    4: "Update existing employee",
    5: "Remove employee",
}


class MenuHandler:

    def __init__(self):
        parent_path = pathlib.Path().resolve()
        self.data_handler = DataHandler(
            json_path=os.path.join(parent_path, "data", "employee.json")
        )
        self.login_handler = LoginHandler(
            json_path=os.path.join(parent_path, "data", "users.json")
        )

    def start_menu(self) -> None:
        print("*"*50)
        print("Hello in the HR Portal!")
        name = input("Please give your name: ")
        user_data = self.login_handler.get_user(name)
        if user_data == {}:
            to_register = input("You are not registered yet! Do you want to be registered? (y/n)")
            if to_register.lower().strip() == "y":
                self.login_handler.save_user(name, 1)
                print(f"You are successfully registered {name}")
                user_level = 1
            else:
                self.login_handler.set_current_user(name, 0)
                user_level = 0
        else:
            print(f"Welcome back {name}")
            self.login_handler.set_current_user(name, 1)
            user_level = 1
        print(f"Your current acces level is: {USER_LEVEL_DICT[user_level]}")

    def main_menu(self):
        possible_options = [1, 2, 3, 4, 5] if self.login_handler.current_user_level else [1, 2, 3]

        for item in possible_options:
            print(f"{item}. {MAIN_MENU_OPTIONS[item]}")
        option = input(f"Give your selection ({', '.join(list(map(lambda x: str(x), possible_options)))}): ").strip()
