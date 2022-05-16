import sys
import os
import pathlib
from .datahandler import DataHandler
from .custom_logging import Logger


class MenuHandler:

    def __init__(self):
        parent_path = pathlib.Path().resolve()
        self.data_handler = DataHandler(
            json_path=os.path.join(parent_path, "data", "data.json")
        )
        self.name = None
        self.exception_logger = Logger(
            json_path=os.path.join(parent_path, "data", "exceptions.log.json")
        )
        self.operation_logger = Logger(
            json_path=os.path.join(parent_path, "data", "operations.log.json")
        )
        self.__start_menu()

    def __get_name_price_input(self) -> [str, int]:
        item_name = input("Please give me the name of the item: ")
        while True:
            try:
                item_price = int(input("Please give me the price of the item: "))
                return item_name, item_price
            except ValueError as ve:
                print("Price must be number")
                self.exception_logger.log({"msg": str(ve)})

    def __start_menu(self) -> None:
        print("*"*50)
        print("Hello in the warehouse!")
        self.name = input("Please give your name: ")
        print(f"Happy to see you {self.name}")

    @staticmethod
    def main_menu() -> int:
        possible_options = [1, 2, 3, 4, 5]
        print("*"*50)
        print("Please select an option")
        print("1. See current inventory")
        print("2. Add new item")
        print("3. Update existing item price")
        print("4. Delete item")
        print("5. Exit warehouse")
        option = input("Give your selection (1,2,3,4,5): ")
        if option.isdigit():
            option = int(option)
            if option not in possible_options:
                raise LookupError(f"{option} is not valid. Available options: {', '.join(map(str, possible_options))}")
            else:
                return option
        else:
            raise ValueError(f"{option} is not a number")

    def add_menu(self) -> None:
        item_name, item_price = self.__get_name_price_input()
        try:
            msg = self.data_handler.add_item(item_name, item_price)
            print(msg)
            self.operation_logger.log({
                "name": self.name, "operation": "item_add",
                "success": True, "values": [item_name, item_price]})
        except ValueError as ve:
            self.exception_logger.log({"msg": str(ve)})
            print(str(ve))
            while True:
                yes_no = input("Do you want to update the price of the item? (y/n): ")
                if yes_no == "n":
                    self.operation_logger.log({
                        "name": self.name, "operation": "item_add",
                        "success": False, "values": [item_name, item_price]})
                    return
                elif yes_no == "y":
                    msg, prev_price = self.data_handler.update_item(item_name, item_price)
                    print(msg)
                    self.operation_logger.log({
                        "name": self.name, "operation": "item_update", "success": True,
                        "values": [item_name, prev_price, item_price]})
                    return
        except Exception as e:
            self.exception_logger.log({"msg": str(e)})

    def update_menu(self):
        item_name, item_price = self.__get_name_price_input()
        try:
            msg, prev_price = self.data_handler.update_item(item_name, item_price)
            print(msg)
            self.operation_logger.log({
                "name": self.name, "operation": "item_update",
                "success": True, "values": [item_name, prev_price, item_price]})
        except ValueError as ve:
            self.exception_logger.log({"msg": str(ve)})
            print(str(ve))
            while True:
                yes_no = input("Do you want to add is as a new item? (y/n): ")
                if yes_no == "n":
                    self.operation_logger.log({
                        "name": self.name, "operation": "item_update",
                        "success": False, "values": [item_name, None, item_price]})
                    return
                elif yes_no == "y":
                    msg = self.data_handler.add_item(item_name, item_price)
                    print(msg)
                    self.operation_logger.log({
                        "name": self.name, "operation": "item_add", "success": True,
                        "values": [item_name, item_price]})
                    return
        except Exception as e:
            self.exception_logger.log({"msg": str(e)})

    def remove_menu(self):
        item_name = input("Please give me the name of the item: ")
        try:
            msg = self.data_handler.delete_item(item_name)
            print(msg)
            self.operation_logger.log({
                "name": self.name, "operation": "item_delete",
                "success": True, "values": [item_name]})
        except ValueError as ve:
            print(str(ve))
            self.exception_logger.log({"msg": str(ve)})
        except Exception as e:
            self.exception_logger.log({"msg": str(e)})

    def list_items(self):
        print("{:<15} {:<8}".format('Name', 'Price'))
        for item in self.data_handler.inventory["menu_items"]:
            print("{:<15} {:<8}".format(item["name"], item["price"]))

    def exit_program(self):
        print("Exiting warehouse")
        self.data_handler.write_data()
        sys.exit()


if __name__ == "__main__":
    handler = MenuHandler()
    handler.start_menu()
    handler.add_menu()
    handler.update_menu()
