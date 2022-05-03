def main():
    print("Welcome to the Warehouse Application!")
    inventory = create_stock_inventory()
    main_menu(inventory)


def main_menu(inventory):
    """
    Main menu of the program
    :param inventory:
    :return:
    """

    while True:
        choose_menu = input("Choose a menu:\n1 - ADD/UPDATE Product \n2 - DELETE product \n"
                            "3 - LIST products\n4 - EXIT\nWrite the number of the menu here: ")
        if choose_menu == "1":
            add_or_update_product(inventory)
        elif choose_menu == "2":
            delete_product(inventory)
        elif choose_menu == "3":
            list_products(inventory)
        elif choose_menu == "4":
            exit_program()
        else:
            print("Not valid value!\n" + "*"*50)


def create_stock_inventory():
    """
    Creates the inventory for the warehouse with a few records
    :return:
    """

    inventory = {
        "window": 30000,
        "door": 67000
    }
    return inventory


def add_or_update_product(inventory):
    """
    Creates a new new item in the warehouse if it doesn't exist yet, otherwise updates the one already in the inventory
    :param inventory:
    :return:
    """
    print("*"*50 + "\nSELECTED MENU: Add or update item.")
    product_name = input("Please add the name of the product: ")
    while True:
        try:
            product_value = int(input("Please add the value of the product: "))
        except ValueError:
            print("Value must be a number!\n" + "*"*50)
            continue
        if type(product_value) != int:
            print("here")
            print("Value must be a number!\n"  + "*"*50)
            product_value = input("Please add the value of the product: ")
        else:
            print(f"SUCCESSFULL ADDITION\nThe new product is: {product_name} and its value is: {product_value}\n"
                  + "*" * 50
                  )
            break

    inventory[product_name] = product_value


def delete_product(inventory):
    print("*"*50 + "\nSELECTED MENU: Delete item.")
    """
    Deletes a product from the warehouse inventory
    :param inventory:
    :return:
    """
    product_to_delete = input("Which product do you want to delete? ")
    try:
        inventory.pop(product_to_delete)
        print(f"SUCCESSFUL DELETION\n{product_to_delete} is deleted.\n" + "*"*50)
    except:
        print("DELETION FAILURE\nThe is no such product\n" + "*" * 50)


def list_products(inventory):
    """
    Lists the items in the warehouse inventory.
    :param inventory:
    :return:
    """
    print("*" * 50 + "\nSELECTED MENU: Add or update item.")
    print("Items in the warehouse inventory:")
    for i in inventory:
        print(str(i) + ": " + str(inventory[i]) + " Ft.")
    print("*"*50)


def exit_program():
    """
    Exits the program after confirm
    """
    while True:
        quit_or_not = input("Are you sure you want to quit? y - exit; n - cancel exit: ")
        if quit_or_not == "y":
            print("Good bye!")
            quit()
        if quit_or_not == "n":
            break
        else:
            print("y/n are the valid values here.\n" + "*"*50)


main()