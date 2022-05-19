class Menu:

    var1: str = "JAJA"

    def __init__(self):
        pass

    def inheritance_method(self):
        print(self.var1)
        self.second_method()

    def second_method(self):
        pass

    @staticmethod
    def menu():
        while True:
            print("")
