def main():
    inventory = create_inventory()
    menu_cycle(inventory)


def create_inventory():
    mydict = {
        "window": 78000,
        "door": 60000
    }
    return mydict


def menu_cycle(inventory):
    while True:
        print('Menu: \n0 : Print catalog\n1 : Add/Modify\n2 : Delete\n3 : Quit')
        myinput = input('Choose a menu: ')
        match myinput:
            case '0':
                print(inventory)
            case '1':
                new_key = input('Name of product: ')
                new_value = input('Value of product: ')
                try:
                    inventory[new_key] = int(new_value)
                    print(f'Successfully added {new_key}, with a value of {new_value}')
                except ValueError:
                    print('You need to put value here! (number)')
            case '2':
                key_to_delete = input('Product name to delete: ')
                try:
                    inventory.pop(key_to_delete)
                    print('Delete successful')
                except:
                    print('There is no such product in the database')
            case '3':
                break


main()
