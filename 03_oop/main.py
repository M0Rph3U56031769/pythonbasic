import datetime

from feature import Feature


class MainClass:

    def __init__(self):
        FeatureInstance = Feature()
        FeatureInstance.print_line()

    @staticmethod
    def print_message():
        Feature.print_hello()


if __name__ == "__main__":
    print(__name__)
    MainInstance = MainClass()
    print(datetime.datetime.now())
    MainInstance.print_message()
