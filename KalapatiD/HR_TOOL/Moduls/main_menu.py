from HR_TOOL.Moduls.add_update_member import AddOrUpdate
from HR_TOOL.Moduls.delete_member import DeleteMember
from HR_TOOL.Moduls.exit_program import ExitProgram
from HR_TOOL.Moduls.list_member import ListMember


class MainMenu:

    @staticmethod
    def selector():
        """
        Menu of the warehouse
        :param warehouse:
        :return:
        """
        while True:
            chose_option = input("Choose a menu:\n1 - Member sign up \n2 - Delete member "
                                 "\n3 - Member list \n4 - Exit\nChoose a menu: ")
            if chose_option == "1":
                add = AddOrUpdate()
                add.create_or_update_member()
            elif chose_option == "2":
                delete = DeleteMember()
                delete.delete_member()
            elif chose_option == "3":
                ListMember.list_members()
            elif chose_option == "4":
                ExitProgram.exit_program()
            else:
                print("Value not okay\n" + "*" * 50)
