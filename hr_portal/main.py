import json
import re
import time
from datetime import date
from datetime import datetime


# TODO: username vs teljes nev
# TODO: login ,remember me dolgot megoldani: Ötlet: jsonbe kiírni hogy remember me: user name , password , a login pedig ezt automatice beolvasná,
# TODO: oop-sítás->fájlokba szétszedés

def file_reading():
    f = open('../data/db.json')
    data = json.load(f)
    f.close()
    # print(type(data)) #dict
    # print(data)
    return data


def file_writing(data):
    with open('../data/db.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def program():
    while True:
        menu()


def listing():
    db = file_reading()
    print("The DB contains the following users:")
    print(db)


def remove():
    pass


def modify():
    pass


def search():
    pass


def menu():
    print("1: ADD\n2. REMOVE\n3. Modify\n4. List\n5. Search")
    n = input("Please give me the number of the requested function: ")
    if n == "1":
        add()
        print(20 * '-')
    elif n == "2":
        remove()
        print(20 * '-')

    elif n == "3":
        modify()
        print(20 * '-')

    elif n == "4":
        listing()
        print(20 * '-')

    elif n == "5":
        search()
        print(20 * '-')

    else:
        print("Invalid menu number")
        print(20 * '-')


def add():
    print("Here you can add a new Person to the database!")
    print("Please give me the following data:")

    valid_name = False

    while valid_name is False:
        name = input(
            "Name: (Please don't use accented letters,only ENGLISH letters) ")  # nem lehet benne szám egyéb spec. karakter , HIBÁT dob á -ra
        x = re.findall("[^\sa-zA-Z]", name)
        if x:
            print("Invalid name!")
            valid_name = False

        else:
            valid_name = True

    valid_bday = False

    while valid_bday is False:
        try:
            bday = input("birthday (YYYY.MM.DD): ")
            bday = bday.replace(" ", "")  # in case of " 1998.05.30" or "1998.05.30 "
            x = re.findall("^[0-2][0-9][0-9][0-9].[0-9][0-9].[0-9][0-9]$", bday)

            if x:
                today = date.today()
                today = today.strftime("%Y.%m.%d")
                today = datetime.strptime(today, '%Y.%m.%d')
                bday = datetime.strptime(bday, '%Y.%m.%d')
                age = today.year - bday.year - ((today.month, today.day) < (bday.month, bday.day))

                if age < 100:  # nem lehet 100 évnél idősebb
                    valid_bday = True
                else:
                    raise ValueError

            else:
                raise ValueError
        except Exception as e:
            print("Invalid birthday date!")
            valid_bday = False

    position = input("position: ")
    organisation = input("organisation: ")
    password = input("password: ")
    phone_number = input("Phone number: ")  # pl 06308539755
    description = input("Description (not obligatory): ")
    db = file_reading()
    db_length = len(db)
    db_elements = list(db[str(db_length)].keys())
    db_elements_dict = {'name': name, 'birthday': bday, 'position': position, 'organisation': organisation,
                        'password': password, 'description': description, 'phone_number': phone_number}
    db.update({str(db_length + 1): db_elements_dict})
    file_writing(db)
    print(db)



program()
