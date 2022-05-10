from .datahandling import DataHandling


class AddOrUpdate:

    @staticmethod
    def add_or_update_product():

        """
        Creates a new new item in the warehouse if it doesn't exist yet, otherwise updates the one already in the inventory
        :param inventory:
        :return:
        """
        handler = DataHandling()
        inventory = handler.read_json()
        print("*"*50 + "\nSELECTED MENU: Add or update item.")

        # check if the name is already in the database
        product_name_list = []
        for ids in inventory:
            for key in inventory[ids]:
                product_name_list.append(key)
        print(product_name_list)
        product_name = input("Please add the name of the product: ")
        if product_name in product_name_list:
            to_be_updated = True
            print("*"*50 + "\nProduct already exists in database. UPDATING product in database")
        else:
            to_be_updated = False
            print("*"*50 + "\nProduct is not in database. CREATING new product in database")

        # get the product value from tha user - must be int, validate
        while True:
            try:
                product_value = int(input("Please add the value of the product: "))
            except ValueError:
                print("Value must be a number!\n" + "*"*50)
                continue
            if type(product_value) != int:
                print("Value must be a number!\n" + "*"*50)
            else:
                print(f"SUCCESSFUL ADDITION\nThe new product is: {product_name} and its value is: {product_value}\n"
                      + "*" * 50
                      )
            break

        # # add unique ID if not in list, else update existing
        # if to_be_updated:
        #     # print(inventory[product_name])
        #     for item in inventory:
        #         for k in inventory.values():
        #             temp = list(k)[0]
        #             if temp == product_name:
        #                 print("hello")
        #                 print(inventory[temp])
        #                 # inventory[] = {product_name: product_value}

        product_id_list = []
        for item in inventory:
            product_id_list.append(item)
        product_id = handler.product_counter() + 1
        while product_id in product_id_list:
            product_id += 1

        inventory[product_id] = {product_name: product_value}

        handler.write_json(inventory)
