def add_modify_item(inv: dict):
    """

    """
    item_name = input("Give me the name of the item: ")
    while True:
        item_price = input("Give me the name price the item: ")
        if item_price.isdigit():
            item_price = int(item_price)
            break

    if item_name in inv.keys():
        print(f"{item_name} found in inventory, modifying value")
    else:
        print(f"Adding {item_name} to directory")

    inv[item_name] = item_price


def del_item(inv: dict):
    inv_keys = inv.keys()
    if len(inv_keys) == 0:
        print("No items in your inventory")
        return

    print(f"Available items: {', '.join(inv_keys)}")
    item_name = input("Give me the name of the item you want to remove: ")
    if item_name not in inv_keys:
        print(f"{item_name} not found in your inventory")
    else:
        inv.pop(item_name)


def inventory_handler():
    print("Lets get ready to rumble (in the inventory)")
    inventory = dict()
    while True:
        print("Please select a menu option")
        menu_val = input("1. Add/Modify, 2. Remove, 3. Exit")
        if not menu_val.isdigit():
            print("Please select a valid value (1, 2, 3)")
            continue
        if menu_val == "1":
            add_modify_item(inventory)
        elif menu_val == "2":
            del_item(inventory)
        elif menu_val == "3":
            print("Exiting from your inventory")
            break


if __name__ == '__main__':
    inventory_handler()
