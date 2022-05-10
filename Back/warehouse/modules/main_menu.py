from .add_or_update_product import AddOrUpdate
from .delete_product import DeleteProduct
from .list_products import ListProducts
from .exit import Exit


class MainMenu:
    @staticmethod
    def selector() -> None:
        """
        Main menu of the program
        :param inventory:
        :return:
        """

        while True:
            choose_menu = input("Choose a menu:\n1 - ADD/UPDATE Product \n2 - DELETE product \n"
                                "3 - LIST products\n4 - EXIT\nWrite the number of the menu here: ")
            if choose_menu == "1":
                AddOrUpdate.add_or_update_product()
            elif choose_menu == "2":
                DeleteProduct.delete_product()
            elif choose_menu == "3":
                ListProducts.list_products()
            elif choose_menu == "4":
                Exit.exit_program()
            else:
                print("Not valid value!\n" + "*" * 50)
