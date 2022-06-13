from .datahandling import DataHandling
from .logger import Logger


class DeleteProduct:

    logger = Logger()
    handler = DataHandling()
    inventory = handler.read_json()

    def delete_product(self):
        """
        Deletes a product from the warehouse inventory
        :return:
        """

        print("*" * 50 + "\nSELECTED MENU: Delete item.")
        product_id_to_delete = input("Which product do you want to delete? ")

        try:
            self.inventory.pop(product_id_to_delete)
            print(f"SUCCESSFUL DELETION\n{product_id_to_delete} is deleted.\n" + "*" * 50)
        except KeyError:
            print("DELETION FAILURE\nThere is no such product\n" + "*" * 50)
            # error = str(KeyError)
            # self.logger.log_delete_key_error(error)
        self.handler.write_json(self.inventory)
