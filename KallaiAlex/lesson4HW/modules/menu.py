try:
    import logging
    import inventory
except:
    from modules import logging
    from modules import inventory
import os

class Menu:
    """
    This class collects the menu functions for the inventory program
    """

    def __init__(self) -> bool:
        # Set up logging
        self.logger = logging.Logging(False)

        # Set up inventory
        self.inv = inventory.Inventory()

        # Get username
        self.username = os.getlogin()

    def mainloop(self) -> None:
        print(f"Hello {self.username}!")
        print(f"Please note that all the changes you make will be logged along with your username.")
        while True:
            print("Inventory application:")
            print("0. List all added items")
            print("1. Modify item")
            print("2. Add new item")
            print("3. Delete item")
            print("4. Check out item")

            selected_option: int = int(input("Please select an option and press enter!\n"))

            if selected_option == 0:
                Menu.listallitems()
            elif selected_option == 1:
                Menu.modifyitem()
            elif selected_option == 2:
                Menu.addnewitem()
            elif selected_option == 3:
                Menu.deleteitem()
            elif selected_option == 4:
                Menu.checkoutitem()
            else:
                print("Please choose one of the options above!")
                print("\n")

    def listallitems(self) -> bool:
        self.inv.listitems()

    def modifyitem(self) -> bool:
        print("Which item would you like to change?")
        name: str = input("Item: ")
        print("To what value?")
        amount: int = int(input("Value: "))
        self.inv.changeitem(name, amount)

    def addnewitem(self) -> bool:
        pass

    def deleteitem(self) -> bool:
        pass

    def checkoutitem(self) -> bool:
        pass
