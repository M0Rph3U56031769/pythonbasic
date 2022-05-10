import json
from functools import wraps

class DataHandler:

    def __init__(self, json_path: str):
        self.json_path = json_path
        self.inventory = None

    def load_data(self):
        with open(self.json_path, "r", encoding="utf-8") as fp:
            self.inventory = json.load(fp)

    def write_data(self):
        with open(self.json_path, "w", encoding="utf-8") as fp:
            json.dump(self.inventory, fp)

    def _get_item(self, name: str) -> (int, str, int):
        for i, item in enumerate(self.inventory["menu_items"]):
            if item["name"] == name:
                return i, item["name"], item["price"]
        else:
            return None

    def delete_item(self, name: str) -> str:
        item = self._get_item(name)
        if item:
            del self.inventory["menu_items"][item[0]]
            msg = f"Successfully deleted {name}"
        else:
            msg = f"No item found with given name {name}"

        self.write_data()
        return msg

    def add_item(self, name: str, price: int):
        item = self._get_item(name)
        if item:
            msg = f"Item already exists with {name} name, updating price"
            self.inventory["menu_items"][item[0]]["price"] = price
        else:
            msg = f"Adding new item with {name} name"
            self.inventory["menu_items"].append({"name": name, "price": price})
        self.write_data()
        return msg


if __name__ == "__main__":
    data_handler = DataHandler(json_path=r"C:\Users\vcsok\Desktop\pythonbasic\vcsokwarehouse\data.json")
    data_handler.load_data()
    print(data_handler.add_item("sanyika", 4234234))
    print(data_handler.delete_item("salami"))
