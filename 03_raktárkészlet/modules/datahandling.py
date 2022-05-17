import json


class DataHandling:

    data: dict = {}
    text: str = ""

    def __init__(self):
        pass

    def read_json(self):
        with open(file="data.json", mode="r", encoding="utf-8") as json_file:
            self.data = json.load(json_file)

    def write_json(self):
        with open(file="data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(self.data, json_file)


MainInstance = DataHandling()
MainInstance.read_json()
