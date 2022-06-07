from .data_handling import DataHandling


class DeleteMember:
    handler = DataHandling()
    inventory = handler.read_json()

    def delete_member(self):

        print("*" * 50 + "\nChoosen Menu: Delete Member")
        """
        Delete member founction!
        """
        product_to_delete = input("Which member would you like delete?")

        try:

            self.logger.log_delete_record_successful(
                self.handler.get_product_name(
                    product_id_to_delete,
                    self.inventory)
            )
            self.inventory.pop(product_id_to_delete)
            print(f"Successful delete!\n {product_to_delete} deleted. \n" + "*" * 50)
        except KeyError:
            print("Unsuccessful delete!\n No such a member\n" + "*" + 50)
            self.logger.log_delete_record_successful()
        self.handler.write_json(self.inventory)

    def confirm_deletion(self, item_to_delete):
        while True:
            confirm_deletion = input(f"Are you sure?"
                                     f": {self.handler.get_product_name(item_to_delete, self.inventory)}"
                                     f"\ny - delete; n - cancel exit: ")
            if confirm_deletion == "y":
                decision = True
            if confirm_deletion == "n":
                break
            else:
                print("y/n only acceptable\n" + "*" * 50)

            return decision
