class Feature:
    line_char: str = "#"

    def print_line(self):
        print(self.line_char * 50)
        print(__name__)

    @staticmethod
    def print_hello():
        print("Hello World!")
        print(__name__)


if __name__ == "__main__":
    Feature.print_hello()
