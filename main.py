import datetime

truefalse: bool = True


def hello_xy(name: str = "asddasvlxckjv") -> str:
    print("#"*50)

    if truefalse:
        print("True")
    if not truefalse:
        print("False")

    if name == "asddasvlxckjv":
        name = input("What is your name? ")
        if name == "asd":
            print("[asd]")
    else:
        print("I know you!")
    return f"{datetime.datetime.now()} - Hello {name} !"


print(hello_xy())
print(hello_xy("fdlksjflésdf"))
print(hello_xy(name="aks3148739184"))
