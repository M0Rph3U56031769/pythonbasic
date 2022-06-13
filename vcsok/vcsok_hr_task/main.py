import sys
from vcsok.vcsok_hr_task.modules.menuhandler import MenuHandler

if __name__ == "__main__":
    menu = MenuHandler()
    menu.start_menu()
    while True:
        try:
            option = menu.main_menu()
        except LookupError as le:
            print(str(le))
            continue
        except Exception as e:
            print(str(e))
            continue
        if option == 0:
            print("Exiting HR Portal")
            sys.exit()
        elif option == 1:
            menu.list_menu()
        elif option == 2:
            menu.search_menu()
        elif option == 3:
            menu.add_menu()
        elif option == 4:
            menu.update_menu()
        elif option == 5:
            menu.remove_menu()
