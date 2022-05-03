import datetime
import time

from pprint import pprint


def dict_test():
    dict_a_thor = {
        "window": 78000,
        "door": 60000,
        "boolean_var": True
    }

    dict_a_thor.pop("door")
    print("#" * 50)
    print(dict_a_thor)
    pprint(dict_a_thor)
    dict_a_thor["window"] = 80000
    print(f"How much is the window: {dict_a_thor.get('window')}")
    print(f"How much is the window: {dict_a_thor['window']}")


def list_and_for_cycle():
    test_list = [
        "e1",
        45,
        123.23,
        [
            "e2",
            "e3"
        ]
    ]

    print(range(5, 10))
    print(len(test_list))

    test_list.append("Appended data")

    for index in range(len(test_list)):
        print(f"{index}: {test_list[index]}")

    print("\n")

    for index, element in enumerate(test_list):
        if type(element) == list:
            print(f"This is a list:")
            for i, e in enumerate(element):
                print(f"\t{i}: {e}")
            print("-" * 50)
        else:
            print(f"{index} - {element}")

def while_true():
    while True:
        timestamp = datetime.datetime.now()
        print(timestamp)

        time.sleep(1)
        # "9" => str(9)
        if "95" in str(timestamp):
            break
    return

while_true()

