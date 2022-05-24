import json
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class FileHandling:

    data: dict

    def read_json(self) -> dict:
        """
        Reads the inventory data from the json file and returns a dict.
        :return dict with inventory data:
        """
        file_path = os.path.join(ROOT_DIR, "data.json")
        with open(file_path, mode="r", encoding="utf-8") as json_file:
            self.data = json.load(json_file)
        return self.data

    def write_json(self):
        """
        Write the dictionary back to the json file.
        :return:
        """
        file_path = os.path.join(ROOT_DIR, "data.json")
        with open(file_path, mode="w", encoding="utf-8") as json_file:
            json.dump(self.data, json_file)
