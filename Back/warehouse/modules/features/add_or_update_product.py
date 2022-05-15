from .datahandling import DataHandling
from .logger import Logger


class AddOrUpdate:
    handler = DataHandling()
    inventory = handler.read_json()
    logger = Logger()

    def create_unique_id(self):
        """
        Generates a new unique ID for the new record and returns is
        :param:
        :return: product_name
        """
        product_id_list = []
        for item in self.inventory:
            product_id_list.append(item)
        product_id = self.handler.product_counter() + 1
        while product_id in product_id_list:
            product_id += 1

        return product_id

    @staticmethod
    def get_product_name_from_user():
        """
        Get name of the product from input
        :param:
        :return: product_name
        """

        print("*" * 50 + "\nSELECTED MENU: Add or update item.")
        product_name = input("Please add the name of the product: ")

        return product_name

    @staticmethod
    def get_product_value_from_user():
        """
        Get value of the product from input - only int is valid
        :param:
        :return: product_value
        """

        product_value = None
        while True:
            try:
                product_value = int(input("Please add the value of the product: "))
            except ValueError:
                print("Value must be a number!\n" + "*" * 50)
                continue
            if type(product_value) != int:
                print("Value must be a number!\n" + "*" * 50)
            else:
                print(f"SUCCESSFUL ADDITION\nThe new product is:  and its value is: {product_value}\n"
                      + "*" * 50
                      )
            break

        return product_value

    def create_or_update_product(self):
        """
        Create a product if not exists yet, and updates if is already in the store
        :param:
        :return: product_value
        """

        product_name = self.get_product_name_from_user()
        if self.decide_upgrading(product_name):
            self.update_product(product_name, self.get_product_value_from_user())
        else:
            self.create_product(product_name, self.get_product_value_from_user())
        self.handler.write_json(self.inventory)

    def create_product(self, product_name, product_value):
        """
        Creates a new record in the store and returns it
        :param: product_name, product_value
        :return: self.inventory
        """

        product_id = self.create_unique_id()
        self.inventory[product_id] = {product_name: product_value}
        self.logger.log_new_record(product_name, product_value)
        return self.inventory

    def update_product(self, product_name, product_value):
        key_list = list(self.inventory.keys())
        val_list = list(self.inventory.values())
        """
        Updates a record if it is in the store already
        :param: product_name, product_value
        :return: self.inventory
        """

        for k, v in self.inventory.items():
            pos = val_list.index(v)
            product_id = key_list[pos]

            if product_name == list(v)[0]:
                self.inventory[product_id] = {product_name: product_value}
        self.logger.log_update(product_name, product_value)

        return self.inventory

    def list_product_names(self):
        """
        Creates a list of the elements in the store and returns is
        :param:
        :return: list of the elements of the store
        """

        product_name_list = []
        for ids in self.inventory:
            for key in self.inventory[ids]:
                product_name_list.append(key)

        return product_name_list

    def decide_upgrading(self, product_name):
        """
        Decides if the new record is to be upgraded or to be created
        :param: product_name
        :return: a boolean which decides if it is to be created or refreshed
        """

        product_name_list = self.list_product_names()
        if product_name in product_name_list:
            to_be_updated = True
            print("*" * 50 + "\nProduct already exists in database. UPDATING product in database")
        else:
            to_be_updated = False
            print("*" * 50 + "\nProduct is not in database. CREATING new product in database")

        return to_be_updated
