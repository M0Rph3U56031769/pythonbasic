#!/bin/python

from modules.menu import Menu
from modules.logging import Logging


def main():
    menuInstance = Menu()
    menuInstance.mainloop()


if __name__ == "__main__":
    # Set up logging
    logger = Logging(False)
    main()
