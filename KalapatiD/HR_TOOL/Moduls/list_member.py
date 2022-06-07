from .data_handling import DataHandling


class ListMember:

    @staticmethod
    def list_members():
        """
        List of products
        :return:
        """
        handler = DataHandling()
        inventory = handler.read_json()
        num_of_products = handler.product_counter()

        print("*" * 50 + "\nChoosen Menu: List")
        print(f"This members are found {num_of_products}")
        for item in inventory:
            print(f"Member ID: {item}, value: {inventory[item]}")
        print("*" * 50)
