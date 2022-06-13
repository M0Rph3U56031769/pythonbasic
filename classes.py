# Author: DNAGY

"""
Module is not for import.
"""


class MainClass:
    """
    This class is for practice.
    """

    class_variable: str = "default value"

    def __init__(self, class_variable: str = "Default Argument"):
        self.class_variable = class_variable

    def just_a_method(self):
        print(self.class_variable)

    @staticmethod
    def static_thing():
        """
        this method type will try to reach a class variable without success.
        :param:
        :return:
        """

        try:
            print(self.class_variable)
        except NameError as err:
            print(err)

        print("This is a static method. cannot use class variables")


if __name__ == "__main__":
    instance = MainClass("NonDEF value")
    instance.just_a_method()
    instance.static_thing()

    instance2 = MainClass()
    instance2.just_a_method()
    instance2.static_thing()
