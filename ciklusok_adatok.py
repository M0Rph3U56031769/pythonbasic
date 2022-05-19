#!/usr/bin/python3

import datetime
import time
from pprint import pprint


def dict_test():
    dict_a_thor = {
        "window": 78000,
        "door": 60000,
        "boolean_var": {
            "sub": "asdasd"
        }
    }

    dict_a_thor.pop("door")
    print("#"*50)
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
    for index, ELEM in enumerate(test_list):
        if isinstance(ELEM, list):
            print("This is a list:")
            for index_elem, element in enumerate(ELEM):
                print(f"\t{index_elem}: {element}")
            print("-"*50)
        else:
            print(f"{index} - {ELEM}")


def while_true():
    while True:
        timestamp = datetime.datetime.now()
        print(timestamp)

        time.sleep(1)
        if str(9) in str(timestamp):
            break
    return


while_true()
