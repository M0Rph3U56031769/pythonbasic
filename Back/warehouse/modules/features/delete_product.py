from .datahandling import DataHandling
from .logger import Logger


class DeleteProduct:

    logger = Logger()
    handler = DataHandling()
    inventory = handler.read_json()

    def delete_product(self):

        print("*" * 50 + "\nSELECTED MENU: Delete item.")
        """
        Deletes a product from the warehouse inventory
        :param inventory:
        :return:
        """
        product_id_to_delete = input("Which product do you want to delete? ")

        try:

            self.logger.log_delete_record_successful(
                self.handler.get_product_name(
                    product_id_to_delete,
                    self.inventory),
                self.handler.get_product_value(
                    product_id_to_delete,
                    self.inventory)
            )
            # if self.confirm_deletion(product_id_to_delete) and self.inventory(product_id_to_delete) is not None:
            self.inventory.pop(product_id_to_delete)
            print(f"SUCCESSFUL DELETION\n{product_id_to_delete} is deleted.\n" + "*" * 50)
        except KeyError:
            print("DELETION FAILURE\nThe is no such product\n" + "*" * 50)
            self.logger.log_delete_record_failure()
        self.handler.write_json(self.inventory)

    def confirm_deletion(self, item_to_delete):
        while True:
            confirm_deletion = input(f"Are you sure you "
                                     f"want to delete this item?: {self.handler.get_product_name(item_to_delete, self.inventory)}"
                                     f"\ny - delete; n - cancel exit: ")
            if confirm_deletion == "y":
                decision = True
            if confirm_deletion == "n":
                break
            else:
                print("y/n are the valid values here.\n" + "*"*50)

            return decision


