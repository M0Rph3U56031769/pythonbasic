from .datahandling import DataHandling
from .logger import Logger


class DeleteProduct:

    logger = Logger()

    def delete_product(self):
        handler = DataHandling()
        inventory = handler.read_json()
        print("*" * 50 + "\nSELECTED MENU: Delete item.")
        """
        Deletes a product from the warehouse inventory
        :param inventory:
        :return:
        """
        product_to_delete = input("Which product do you want to delete? ")
        try:
            print(len(list(inventory.keys())))
            print(product_to_delete)
            self.logger.log_delete_record_successful(
                list(inventory.keys())[int(product_to_delete)],
                list(inventory.values())[int(product_to_delete)])
            inventory.pop(product_to_delete)
            print(f"SUCCESSFUL DELETION\n{product_to_delete} is deleted.\n" + "*" * 50)
        except KeyError:
            print("DELETION FAILURE\nThe is no such product\n" + "*" * 50)
        handler.write_json(inventory)
