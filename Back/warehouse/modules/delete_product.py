from .datahandling import DataHandling


class DeleteProduct:

    @staticmethod
    def delete_product():

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
            inventory.pop(product_to_delete)
            print(f"SUCCESSFUL DELETION\n{product_to_delete} is deleted.\n" + "*" * 50)
        except:
            print("DELETION FAILURE\nThe is no such product\n" + "*" * 50)

        handler.write_json(inventory)
