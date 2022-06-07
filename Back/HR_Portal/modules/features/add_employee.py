from .datahandling import DataHandling
import datetime


class AddEmployee:
    handler = DataHandling()
    inventory = handler.read_json()

    def add_employee(self):
        name = self.get_name()
        birthday = self.get_birthday()
        position = self.get_position()
        organisation = self.get_organisation()
        password = self.get_password()
        description = self.get_description()
        phone_number = self.get_phone_number()

        self.inventory[name] = [{"birthday": birthday},
                                {"position": position},
                                {"organization": organisation},
                                {"password": password},
                                {"description": description},
                                {"phone_number": phone_number}
                                ]

        self.handler.write_json(self.inventory)

    @staticmethod
    def get_name() -> str:
        return input("Give employee name:")

    @staticmethod
    def get_birthday() -> datetime:
        return input("Give birthday:")

    @staticmethod
    def get_position() -> str:
        return input("Give position:")

    @staticmethod
    def get_organisation() -> str:
        return input("Give organisation:")

    @staticmethod
    def get_password() -> str:
        return input("Give password:")

    @staticmethod
    def get_description() -> str:
        return input("Give description:")

    @staticmethod
    def get_phone_number() -> int:
        return input("Give phone number:")
