"""
Készlet:
Ajtó: 30000 Ft
Ablak: 67000 Ft
"""

keszlet = {
    "Ajtó": 30000,
    "Ablak": 67000,
}


def almenu():
    print("Hozzáadni szeretnél vagy módosítani?")
    menuszam = input("1. Hozzáadás\n2. Módosítás\n")
    if menuszam == "1":
        hozzadas()
    elif menuszam == "2":
        modositas()
    else:
        print("Ismeretlen menüszám!")


def lista():
    for elem in keszlet:
        print(elem, " --- ", keszlet[elem])


def hozzadas():
    while True:
        print(20 * "*")
        elem_nev = input("Hozzaadandó elem neve: ")
        sikeres_elemfelvetel = True
        while sikeres_elemfelvetel == True:
            try:
                elem_ar = input("Az ára Ft-ban: ")
                keszlet[elem_nev] = int(elem_ar)
                sikeres_elemfelvetel = False
            except:
                print("Nem megfelelő input!")

        print(
            f"A(z) {elem_nev} elem , {elem_ar} árral hozzá lett adva a raktárkészlethez."
        )
        n = input("0. További elemek felvétele\n1. Visszatérés a főmenühöz\n")
        if int(n) == 1:
            return


def modositas():
    while True:
        print(20 * "*")
        elem_nev = input("Add meg a módosítandó elem nevét: ")
        if elem_nev in keszlet:
            sikeres_elemfelvetel = True
            while sikeres_elemfelvetel == True:
                try:
                    elem_ar = input("Add meg az új árat: ")
                    keszlet[elem_nev] = int(elem_ar)
                    print(
                        f"A(z) {elem_nev} elem , {elem_ar} árral hozzá lett adva a raktárkészlethez."
                    )
                    sikeres_elemfelvetel = False
                except:
                    print("Nem megfelelő input!")
        else:
            print("Nincs ilyen elem!.")
        n = input("0. További elemek módosítása\n1. Visszatérés a főmenühöz\n")
        if int(n) == 1:
            return


def torles():
    if len(keszlet) > 0:
        while True:
            print(20 * "*")
            torles_bool = False
            while torles_bool == False:
                elem_nev = input("Add meg,hogy melyik elemet szeretnéd törölni: ")
                if elem_nev in keszlet:
                    torolt_elem = keszlet.pop(elem_nev)
                    print("A(z) {} törölve lett.".format(elem_nev))
                    sikeres_torles = True
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
            almenu()
        elif n == "2":
            torles()
        elif n == "3":
            print(20 * "*")
            break
        elif n == "titok":
            lista()
        else:
            print("Nem létező menüszám!")

    except Exception as e:
        print("ERROR: ", e)
