import json
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class DataHandling:

    data: dict


    def read_json(self) -> dict:
        file_path = os.path.join(ROOT_DIR, "../data/data.json")
        with open(file_path, mode="r", encoding="utf-8") as json_file:
            self.data = json.load(json_file)
        return self.data

    @staticmethod
    def write_json(data):
        file_path = os.path.join(ROOT_DIR, "../data/data.json")
        with open(file_path, mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file ensure_ascii=False, indent=4)
            json_file.write("\n")
