"""
Készlet:
Ajtó: 30000 Ft
Ablak: 67000 Ft
"""

warehouse = {
    "Ajtó": 30000,
    "Ablak": 67000,
}


def submenu():
    print("Hozzáadni szeretnél vagy módosítani?")
    menu_number = input("1. Hozzáadás\n2. Módosítás\n")
    if menu_number == "1":
        add()
    elif menu_number == "2":
        modify()
    else:
        print("Ismeretlen menüszám!")


def listing():
    for item in warehouse:
        print(item, " --- ", warehouse[item])


def add():
    while True:
        print(20 * "*")
        product_name = input("Hozzaadandó elem neve: ")
        succesful_product_recording = True
        while succesful_product_recording == True:
            try:
                product_price = input("Az ára Ft-ban: ")
                warehouse[product_name] = int(product_price)
                succesful_product_recording = False
            except:
                print("Nem megfelelő input!")

        print(
            f"A(z) {product_name} elem , {product_price} árral hozzá lett adva a raktárkészlethez."
        )
        n = input("0. További elemek felvétele\n1. Visszatérés a főmenühöz\n")
        if int(n) == 1:
            return


def modify():
    while True:
        print(20 * "*")
        product_name = input("Add meg a módosítandó elem nevét: ")
        if product_name in warehouse:
            succesful_product_recording = True
            while succesful_product_recording == True:
                try:
                    product_price = input("Add meg az új árat: ")
                    warehouse[product_name] = int(product_price)
                    print(
                        f"A(z) {product_name} elem , {product_price} árral hozzá lett adva a raktárkészlethez."
                    )
                    succesful_product_recording = False
                except:
                    print("Nem megfelelő input!")
        else:
            print("Nincs ilyen elem!.")
        n = input("0. További elemek módosítása\n1. Visszatérés a főmenühöz\n")
        if int(n) == 1:
            return


def delete():
    if len(warehouse) > 0:
        while True:
            print(20 * "*")
            delete_bool = False
            while delete_bool == False:
                product_name = input("Add meg,hogy melyik elemet szeretnéd törölni: ")
                if product_name in warehouse:
                    deleted_product = warehouse.pop(product_name)
                    print("A(z) {} törölve lett.".format(product_name))
                    delete_bool = True
                    return

                else:
                    print("Nincs ilyen elem!.")
    else:
        print("Üres a raktárkészleti adatbázis!")
        print(20 * "*")


while True:
    try:
        n = input(
            "A funkciók eléréséhez írd be a hozzátartozó számot: \n1. Hozzáadás/módosítás\n2. Törlés\n3. Kilépés\n "
        )
        if n == "1":
            submenu()
        elif n == "2":
            delete()
        elif n == "3":
            print(20 * "*")
            break
        elif n == "titok":
            listing()
        else:
            print("Nem létező menüszám!")

    except Exception as e:
        print("ERROR: ", e)
