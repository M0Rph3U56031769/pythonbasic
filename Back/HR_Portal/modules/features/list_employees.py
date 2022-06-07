from .datahandling import DataHandling


class ListEmployees:

    @staticmethod
    def list_employees():

        handler = DataHandling()
        inventory = handler.read_json()

        for item in inventory:
            print(inventory[item])
