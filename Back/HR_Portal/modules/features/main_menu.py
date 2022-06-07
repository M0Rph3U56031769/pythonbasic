from .add_employee import AddEmployee
from .list_employees import ListEmployees


class MainMenu:

    @staticmethod
    def menu_selector():

        while True:
            choose_menu = input("Choose an option!\n" 
                                "Add new employee: - 1\n" 
                                "Remove employee: - 2\n" 
                                "Modify employee: - 3\n" 
                                "List employees: - 4\n" 
                                "Search employee: - 5"
                                )

            if choose_menu == "1":
                add = AddEmployee()
                add.add_employee()
            elif choose_menu == "2":
                raise NotImplementedError
            elif choose_menu == "3":
                raise NotImplementedError
            elif choose_menu == "4":
                listing = ListEmployees()
                listing.list_employees()
            elif choose_menu == "5":
                raise NotImplementedError
            else:
                print("Not valid input!")
