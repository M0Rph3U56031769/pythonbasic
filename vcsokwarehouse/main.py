from modules.menuhandler import MenuHandler

if __name__ == "__main__":
    menu_handler = MenuHandler()
    while True:
        try:
            option = menu_handler.main_menu()
        except LookupError as le:
            print(str(le))
            menu_handler.exception_logger.log({"msg": str(le)})
            continue
        except ValueError as ve:
            print(str(ve))
            menu_handler.exception_logger.log({"msg": str(ve)})
            continue
        except Exception as e:
            menu_handler.exception_logger.log({"msg": str(e)})
            continue

        if option == 1:
            menu_handler.list_items()
        elif option == 2:
            menu_handler.add_menu()
        elif option == 3:
            menu_handler.update_menu()
        elif option == 4:
            menu_handler.remove_menu()
        elif option == 5:
            menu_handler.exit_program()
