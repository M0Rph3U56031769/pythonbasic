import os
import json
from datetime import datetime


class Logger:
    def __init__(self, json_path: str):
        self.json_path = json_path
        self.log_data = None
        self.load_data()

    def load_data(self):
        if not os.path.exists(self.json_path):
            if self.log_data is None:
                self.log_data = dict()
        else:
            with open(self.json_path, 'r') as fp:
                self.log_data = json.load(fp)

    def log(self, data: dict):
        self.log_data[str(datetime.utcnow())] = data
        with open(self.json_path, "w") as fp:
            json.dump(self.log_data, fp, indent=4)
