class ExitProgram:

    @staticmethod
    def exit_program():
        """
        Exit of program
        :return:
        """
        while True:
            quit_or_not = input("Do you want to exit? y - Exit; n - Cancel: ")
            if quit_or_not == "y":
                print("Good bye!")
                quit()
            if quit_or_not == "n":
                break
            else:
                print("y/n Value is not okay\n" + "*" * 50)
