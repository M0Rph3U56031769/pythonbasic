import time

products_dict = {
    "door": 30000,
    "window": 67000
}


def print_prod(products: dict):
    print(f"Product list:")
    for index, (element, price) in enumerate(products.items()):
        print(f"\t{index}: {element}: {price}")  # \t - tabulator"""


def add(element: str, price: int):
    products_dict[element] = price  # Modify/add
    print("Element is added/modified!")


def delete(element: str, products: dict):
    if element in products:
        products_dict.pop(element)  # Remove element
        print("Element is deleted!")
    else:
        print("The typed name doesn't exist!")


def repo(products: dict):  # Infinite loop
    while True:
        print("\n" + "-" * 25 + " Repository program " + "-" * 25)
        print_prod(products)
        option: str = str()
        element: str = str()
        price: int = int()
        print("\nAvailable options: \n A - Add/Modify \n B - Delete \n C - Escape")
        option = input("\nSelect an option: ")
        if option == "A":
            print("\n" + "-" * 25 + " Adding/Modifying " + "-" * 25)
            element = input("Add the name of the element: ")
            price = int(input("Add the price of the element: "))
            add(element, price)
        elif option == "B":
            print("\n" + "-" * 25 + " Deleting " + "-" * 25)
            element = input("Add the name of the element: ")
            delete(element, products)
        elif option == "C":
            print("You escaped from the program")
            break  # Exit from infinite loop
        else:
            print("The typed input is not correct!")
        time.sleep(1)

repo(products_dict)
