from .datahandling import DataHandling


class ListProducts:

    @staticmethod
    def list_products():
        """
        Lists the items in the warehouse inventory.
        :param:
        :return:
        """
        handler = DataHandling()
        inventory = handler.read_json()
        num_of_products = handler.product_counter()

        print("*" * 50 + "\nSELECTED MENU: Add or update item.")
        print(f"Items in the warehouse inventory, number of items: {num_of_products}:")
        for item in inventory:
            print(f"Product ID: {item}, Value: {inventory[item]}")
        print("*" * 50)
