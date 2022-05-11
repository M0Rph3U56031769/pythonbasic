import json
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class DataHandling:

    data: dict

    def read_json(self):

        file_path = os.path.join(ROOT_DIR, "data.json")
        with open(file_path, mode="r", encoding="utf-8") as json_file:
            self.data = json.load(json_file)
        return self.data

    @staticmethod
    def write_json(data):
        file_path = os.path.join(ROOT_DIR, "data.json")
        with open(file=file_path, mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
            json_file.write("\n")

    @staticmethod
    def product_counter():
        file_path = os.path.join(ROOT_DIR, "data.json")
        with open(file_path, mode="r", encoding="utf-8") as json_file:
            inventory = json.load(json_file)
            counter = 0
            for i in inventory:
                counter += 1
        return counter

    @staticmethod
    def validate_unique_id_and_name(inventory, handler):
        product_id_list = []
        for i in inventory:
            product_id_list.append(i)
        product_id = handler.product_counter() + 1

        while product_id in product_id_list:
            product_id += 1
        product_name_list = []

        for ids in inventory:
            for key in inventory[ids]:
                print(key)
        print(product_name_list)
