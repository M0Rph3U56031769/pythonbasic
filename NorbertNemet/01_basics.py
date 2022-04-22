import datetime  # import datetime module


def addName() -> str:
    name: str = input(f"{datetime.datetime.now()} - What is you name? ")  # Input your name
    return name


def welcome(name):
    if name != "":
        print(f"{datetime.datetime.now()} - Welcome {name}!")
    else:
        print(f"{datetime.datetime.now()} - Please add your name!")
        name = addName()
        welcome(name)


yourName = addName()
welcome(yourName)

