import os
import re
import pathlib
from typing import Dict
from .datahandler import DataHandler
from .loginhandler import LoginHandler
from .employee import Employee

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

    @staticmethod
    def __get_name():
        """
        Asks for the employee name
            Returns:
                name (str): employee name
        """
        while True:
            name = input("Please give employee name: ").strip()
            if name == "":
                print("Employee name can not be empty")
            else:
                return name

    @staticmethod
    def __get_user_key(available_keys: list, action: str):
        """
        Asks for the uuid key of a user
        Parameters:
            available_keys (list): keys that are available so user input can be verified
            action (str): action string to fill in prop message
        """
        while True:
            employee_key = input(f"Please give the key of the employee you want to {action}: ").strip()
            if employee_key not in available_keys:
                print(f"{employee_key} is not a valid key, possible keys: {', '.join(available_keys)}")
            else:
                return employee_key

    @staticmethod
    def __get_birth_day(can_be_empty: bool = False) -> str:
        """
        Asks for the employee birthday with format verification
            Parameters:
                can_be_empty (bool): if True the value can be skipped
            Returns:
                (string): dateinput
        """
        while True:
            birth_day = input("Please give employee birth day (YYYY/MM/DD): ").strip()
            if re.match("[0-9]{4}\/[0-9]{2}\/[0-9]{2}", birth_day):
                return birth_day
            elif birth_day == "" and can_be_empty:
                return birth_day
            else:
                print("Invalid date format. Format must be (YYYY/MM/DD)")

    @staticmethod
    def __get_basic_value(value_name: str, can_be_empty: bool = False) -> str:
        """
        Asks for the employee value with optional input
            Parameters:
                value_name (str): name of the employee value to fill the prop
                can_be_empty (bool): if True the value can be skipped
            Returns:
                (string): user input
        """
        while True:
            value = input(f"Please give employee {value_name}: ").strip()
            if value == "" and not can_be_empty:
                print(f"{value_name.capitalize()} can not be empty")
            else:
                return value

    def __get_employee_details(self) -> Dict:
        """
        Asks for the employee details from the user with the fields not optional
            Returns:
                (dict): return input dictionary in Employee parsable format
        """
        name = self.__get_name()
        birth_day = self.__get_birth_day()
        position = self.__get_basic_value("position")
        organisation = self.__get_basic_value("organisation")
        password = self.__get_basic_value("password")
        phone_number = self.__get_basic_value("phone_number")
        description = self.__get_basic_value("description", can_be_empty=True)
        return {
            "name": name, "birth_day": birth_day,
            "position": position, "organisation": organisation,
            "password": password, "phone_number": phone_number,
            "description": description
        }

    def __get_employee_details_optional(self) -> Dict:
        """
        Asks for the employee details from the user with the fields optional
            Returns:
                (dict): return input dictionary in Employee parsable format
        """
        name = self.__get_name()
        birth_day = self.__get_birth_day(can_be_empty=True)
        position = self.__get_basic_value("position", can_be_empty=True)
        organisation = self.__get_basic_value("organisation", can_be_empty=True)
        password = self.__get_basic_value("password", can_be_empty=True)
        phone_number = self.__get_basic_value("phone_number", can_be_empty=True)
        description = self.__get_basic_value("description", can_be_empty=True)
        return {
            "name": name, "birth_day": birth_day,
            "position": position, "organisation": organisation,
            "password": password, "phone_number": phone_number,
            "description": description
        }

    def start_menu(self) -> None:
        """
        Triggers the start menu
        """
        print("*" * 50)
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

    def main_menu(self) -> int:
        """
        Triggers the main menu
        """
        possible_options = [0, 1, 2, 3, 4, 5] if self.login_handler.current_user_level else [0, 1, 2]

        for item in possible_options:
            print(f"{item}. {MAIN_MENU_OPTIONS[item]}")
        option = input(f"Give your selection ({', '.join(list(map(lambda x: str(x), possible_options)))}): ").strip()
        try:
            option = int(option)
            if option not in possible_options:
                raise ValueError
            return int(option)
        except ValueError as e:
            raise LookupError(
                f"{option} is not valid. Available options: {', '.join(map(str, possible_options))}")

    def add_menu(self) -> None:
        """
        Triggers the add menu
        """
        print("Add Menu")
        employee_values = self.__get_employee_details()
        with_same_name = self.data_handler.get_item(employee_values["name"])
        if with_same_name != {}:
            print("Found employees with same name:")
            for key, employee in with_same_name.items():
                print("-"*50)
                print(f"Employee ID: {key}")
                print(employee)
            to_update = input("Do you want to update one of them? (y/n)").strip().lower()
            if to_update == "y":
                employee_key = self.__get_user_key(list(map(lambda x: str(x), with_same_name.keys())), "update")
                self.data_handler.update_item(employee_key, **employee_values)
                print("Updated employee")
            else:
                self.data_handler.add_item(**employee_values)
                print("Added employee")
        else:
            self.data_handler.add_item(**employee_values)
            print("Added employee")

    def list_menu(self) -> Dict[str, Employee]:
        """
        Triggers the list menu
            Returns:
                (dict): Returns the available employees (uuid string, employee)
        """
        print("Available employees:")
        available_employees = self.data_handler.get_item()
        if available_employees != {}:
            for key, employee in available_employees.items():
                print("-" * 50)
                print(f"Employee ID: {key}")
                print(employee)
        else:
            print("No available employees")
        return available_employees

    def update_menu(self) -> None:
        """
        Triggers the update menu
        """
        print("Update Menu")
        available_employees = self.list_menu()
        if available_employees == {}:
            to_add = input("Do you want to add new employee? (y/n)").strip().lower()
            if to_add == "y":
                self.add_menu()
        else:
            employee_key = self.__get_user_key(list(map(lambda x: str(x), available_employees.keys())), "update")
            employee_values = self.__get_employee_details_optional()
            self.data_handler.update_item(employee_key, **employee_values)
            print("Updated employee")

    def remove_menu(self):
        """
        Triggers the remove menu
        """
        print("Remove Menu")
        available_employees = self.list_menu()
        if available_employees == {}:
            to_add = input("Do you want to add new employee? (y/n)").strip().lower()
            if to_add == "y":
                self.add_menu()
        else:
            employee_key = self.__get_user_key(list(map(lambda x: str(x), available_employees.keys())), "delete")
            to_delete = input("Are you sure you want to delete the selected employee? (y/n) ").strip().lower()
            if to_delete == "y":
                self.data_handler.delete_item(employee_key)
            else:
                print("Skipping deletion")

    def search_menu(self):
        """
        Triggers the search menu
        """
        print("Search Menu")
        name = self.__get_basic_value("name")
        available_employees = self.data_handler.get_item(name)
        if available_employees != {}:
            print("Found employees with same name:")
            for key, employee in available_employees.items():
                print("-"*50)
                print(f"Employee ID: {key}")
                print(employee)
        else:
            print("No employee found with given name")
