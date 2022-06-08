from .datahandling import Datahandling


class Menu:

    data_instance = Datahandling()

    def menu_selector(self):
        """
        Draws a menu list. Waits for an input to the selected menu and starts the selected method.
        :return:
        """
        while True:
            print("=" * 50)
            print("Menu:\n1. Add/Edit element\n2. Delete element\n3. List elements")
            menu_button = input("Enter a menu a number: ")
            if menu_button == "1":
                self.menu_add_edit()
            elif menu_button == "2":
                self.menu_delete()
            elif menu_button == "3":
                self.menu_list()
            else:
                print("Wrong button!")
            self.data_instance.save()

    def menu_add_edit(self):
        """
        Reads a name and price value from the user then calls the add or edit methods.
        :return:
        """
        name = input("Enter the name of the element you want to add or edit: ")
        if self.data_instance.existing(name):
            d_id = self.data_instance.name_id(name)
            print("This name is already added. Current price: ", self.data_instance.inventory[d_id]["price"])
            y_n = input("Do you want to edit? (y/n): ")
            if y_n == "y":
                price = input(f"Enter a price for {name}: ")
                self.data_instance.edit_element(name, price)
                print(f"Price for {name} has been edited successfully.")
        else:
            price = input(f"Enter a price for {name}: ")
            self.data_instance.add_element(name, price)
            print("New entry has been added successfully.")

    def menu_delete(self):
        """
        Reads the name value from the use then calls the delete method.
        :return:
        """
        name = input("Enter the name of the element you want to delete: ")
        if self.data_instance.existing(name):
            y_n = input(f"Are you sure to delete {name}? (y/n): ")
            if y_n == "y":
                self.data_instance.delete_element(name)
                print(f"{name} has been deleted successfully")
        else:
            print("The entered name is not in the database!")

    def menu_list(self):
        """
        Calls the data listing method in a pretty way.
        :return:
        """
        print("=" * 50)
        self.data_instance.list_elements()
