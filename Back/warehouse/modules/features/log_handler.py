import json
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class LogHandler:

    op_log_data: dict
    ex_log_data: dict

    def read_operation_log_file(self):
        file_path = os.path.join(ROOT_DIR, "../logs/operations.log.json")
        with open(file_path, mode="r", encoding="utf-8") as json_file:
            self.op_log_data = json.load(json_file)
        return self.op_log_data

    @staticmethod
    def write_op_log_file(op_log_data):
        file_path = os.path.join(ROOT_DIR, "../logs/operations.log.json")
        with open(file=file_path, mode="w", encoding="utf-8") as json_file:
            json.dump(op_log_data, json_file, ensure_ascii=False, indent=4)
            json_file.write("\n")

    def read_exception_log_file(self):
        file_path = os.path.join(ROOT_DIR, "../logs/exceptions.log.json")
        with open(file_path, mode="r", encoding="utf-8") as json_file:
            self.ex_log_data = json.load(json_file)
        return self.ex_log_data

    @staticmethod
    def write_ex_log_file(ex_log_data):
        file_path = os.path.join(ROOT_DIR, "../logs/exceptions.log.json")
        with open(file=file_path, mode="w", encoding="utf-8") as json_file:
            json.dump(ex_log_data, json_file, ensure_ascii=False, indent=4)
            json_file.write("\n")




