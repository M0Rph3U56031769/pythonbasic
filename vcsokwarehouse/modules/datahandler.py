import json
import os


class DataHandler:

    def __init__(self, json_path: str):
        self.json_path = json_path
        self.inventory = None
        self.load_data()

    def load_data(self):
        if not os.path.exists(self.json_path):
            if self.inventory is None:
                self.inventory = {"menu_items": []}
        else:
            with open(self.json_path, "r", encoding="utf-8") as fp:
                self.inventory = json.load(fp)

    def write_data(self):
        with open(self.json_path, "w", encoding="utf-8") as fp:
            json.dump(self.inventory, fp)

    def __get_item(self, name: str) -> (int, str, int):
        for i, item in enumerate(self.inventory["menu_items"]):
            if item["name"] == name.lower():
                return i, item["name"], item["price"]
        else:
            return None

    def delete_item(self, name: str) -> str:
        item = self.__get_item(name)
        if item:
            del self.inventory["menu_items"][item[0]]
            msg = f"Successfully deleted {name}"
        else:
            raise ValueError(f"No item found with given name {name}")
        self.write_data()
        return msg

    def add_item(self, name: str, price: int) -> str:
        item = self.__get_item(name)
        if item:
            raise ValueError("Item found with given name")
        else:
            msg = f"Adding new item with {name} name"
            self.inventory["menu_items"].append({"name": name.lower(), "price": price})
        self.write_data()
        return msg

    def update_item(self, name: str, price: int) -> (str, int):
        item = self.__get_item(name)
        if item:
            msg = f"Updated price for item with {name} name"
            prev_price = self.inventory["menu_items"][item[0]]["price"]
            self.inventory["menu_items"][item[0]]["price"] = price
        else:
            raise ValueError("Item not found with given name")
        self.write_data()
        return msg, prev_price


if __name__ == "__main__":
    data_handler = DataHandler(json_path=r"C:\Users\vcsok\Desktop\pythonbasic\vcsokwarehouse\data\data.json")
    data_handler.load_data()
    print(data_handler.update_item("Sanyika", 4234234))
    print(data_handler.delete_item("salami"))
