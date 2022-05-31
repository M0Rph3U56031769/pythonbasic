class Exit:

    @staticmethod
    def exit_program():

        """
        Exits the program after confirm
        """
        while True:
            quit_or_not = input("Are you sure you want to quit? y - exit; n - cancel exit: ")
            if quit_or_not == "y":
                print("Good bye!")
                quit()
            if quit_or_not == "n":
                break
            else:
                print("y/n are the valid values here.\n" + "*"*50)
