
volvo_dict = {
    "Engine": 1000,
    "Chassis": 5000,
    "Transmission": 800,
    "Suspension": 2500
}

def add_element() -> str:
    print("=" * 50)
    key = input("Enter the name of the new entry: ")
    value = input("Enter the price of the new entry: ")
    volvo_dict[key] = value
    return "New entry added successfully!"

def delete_element() -> str:
    while True:
        print("=" * 50)
        key = input("Enter the name of the entry that you want to remove: ")
        if volvo_dict.get(key) is None:
            print("No such element")
        else:
            volvo_dict.pop(key)
            break
    return f"{key} element is succesfully deleted!"

def edit_element() -> str:
    while True:
        print("=" * 50)
        key = input("Enter the name of the entry that you want to edit: ")
        value = None
        if volvo_dict.get(key) is None:
            print("No such element")
        else:
            print(f"Current value for {key} is: {volvo_dict.get(key)}")
            value = input(f"Enter a new value for {key}: ")
            volvo_dict[key] = value
            break
    return f"{key} element's value successfully refreshed. New value is: {value}"

def list_elements():
    print("=" * 50)
    for item in volvo_dict.items():
        print(item)
    return


while True:
    print("="*50)
    print("Menu:\n1. Add element\n2. Delete element\n3. Edit element\n4. List elements")
    menu_button = input("Enter a menu a number: ")
    if menu_button == "1":
        print(add_element())
    elif menu_button == "2":
        print(delete_element())
    elif menu_button == "3":
        print(edit_element())
    elif menu_button == "4":
        list_elements()
    else:
        print("Wrong button!")

