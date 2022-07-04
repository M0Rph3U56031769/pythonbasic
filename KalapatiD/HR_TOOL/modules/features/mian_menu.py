from .add_workers import AddWorkers
from .list_workers import ListWorkers


class MainMenu:

    @staticmethod
    def menu_selector():

        while True:
            select_menu = input("Choose an option!\n""1 - Add new workers!\n""2 - Remove workers!\n"
                                "3 - Modify workers!\n""4 - List workers\n""5 - Search workers")

            if select_menu == "1":
                add = AddWorkers()
                add.add_workers()
            elif select_menu == "2":
                raise NotImplementedError
            elif select_menu == "3":
                raise NotImplementedError
            elif select_menu == "4":
                listing = ListWorkers()
                listing.list_workers()
            elif select_menu == "5":
                raise NotImplementedError
            else:
                print("Not valid input!")