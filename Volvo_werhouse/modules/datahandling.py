from .filehandling import FileHandling


class Datahandling:

    file_instance = FileHandling()
    inventory = file_instance.read_json()

    def name_id(self, name) -> str:
        """
        Returns an ID of the given name.
        :param name:
        :return d_id:
        """
        for d_id, d_info in self.inventory.items():
            for d_name in d_info:
                if d_info[d_name] == name:
                    return d_id

    def existing(self, name) -> bool:
        """
        Decide if the given name is existing in the database.
        :param name:
        :return True: if the name exists, False: if the name not exists:
        """
        if self.name_id(name) is not None:
            return True
        else:
            return False

    def get_new_id(self) -> str:
        """
        Returnes an unused ID for new entries.
        :return Unused ID:
        """
        new_id = 0
        for d_id, d_info in self.inventory.items():
            if new_id == int(d_id):
                new_id += 1

        return str(new_id)

    def add_element(self, name, price):
        """
        Adds a new entry to the database with the given name and price.
        :param name:
        :param price:
        :return:
        """
        self.inventory[self.get_new_id()] = {"name": name, "price": price}

    def delete_element(self, name):
        """
        Deletes the entry of the given name.
        :param name:
        :return:
        """
        del self.inventory[self.name_id(name)]

    def edit_element(self, name, price):
        """
        Edits the price of the given names entry.
        :param name:
        :param price:
        :return:
        """
        self.inventory[self.name_id(name)] = {"name": name, "price": price}

    def list_elements(self):
        """
        List the elements of the Database structured by IDs and keys.
        :return:
        """
        for d_id, d_info in self.inventory.items():
            print("\nID:", d_id)
            for d_key in d_info:
                print(f"{d_key}: {d_info[d_key]}")

    def save(self):
        """
        Saves the current dictionary back to the json file.
        :return:
        """
        self.file_instance.write_json()
