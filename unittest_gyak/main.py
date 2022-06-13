import datetime


class ToBeTested:

    print_message: int = 0

    def print_number(self, number: int = 42):
        self.print_message = number
        print(number)
        return number

    @staticmethod
    def print_timestamp():
        return datetime.datetime.now()
