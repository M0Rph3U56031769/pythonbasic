import json
import os
import uuid
from typing import Dict
from datetime import datetime, date
from .employee import Employee


class DataHandler:

    def __init__(self, json_path: str):
        self.json_path = json_path
        self.employee_dict = {}
        self.load_data()

    def load_data(self) -> None:
        if os.path.exists(self.json_path):
            with open(self.json_path, "r", encoding="utf-8") as fp:
                loaded_data = json.load(fp)
                for key, value in loaded_data.items():
                    self.employee_dict[key] = Employee.parse_employee(value)

    @staticmethod
    def json_serial(obj) -> None:
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        else:
            return str(obj)

    def write_data(self) -> None:
        with open(self.json_path, "w", encoding="utf-8") as fp:
            temp_inv = {k: vars(v) for k, v in self.employee_dict.items()}
            json.dump(temp_inv, fp, indent=4, default=self.json_serial)

    def get_item(self, name: str = None) -> Dict[str, Employee]:
        ret_dict = {}
        for key, item in self.employee_dict.items():
            if name is None:
                ret_dict[key] = item
            elif item.name.lower() == name.lower():
                ret_dict[key] = item
        return ret_dict

    def delete_item(self, key: str) -> bool:
        try:
            del self.employee_dict[key]
        except KeyError as ke:
            return False
        self.write_data()
        return True

    def add_item(
            self, name: str, birth_day: str, position: str,
            organisation: str, password: str, phone_number: str,
            description: str = None) -> bool:
        employee = Employee.parse_employee({
                "name": name, "birth_day": birth_day,
                "position": position, "organisation": organisation,
                "password": password, "phone_number": phone_number,
                "description": description
        })
        self.employee_dict[str(uuid.uuid4())] = employee
        self.write_data()
        return True

    def update_item(
            self, key: str, name: str = None, birth_day: datetime = None, position: str = None,
            organisation: str = None, password: str = None, phone_number: str = None,
            description: str = None) -> bool:
        try:
            self.employee_dict[key].update_fields({
                "name": name, "birth_day": birth_day,
                "position": position, "organisation": organisation,
                "password": password, "phone_number": phone_number,
                "description": description
            })
        except KeyError as ke:
            return False
        self.write_data()
        return True


if __name__ == "__main__":
    handler = DataHandler(
        json_path=os.path.join(
            r"C:\Users\csokviktor\Desktop\pythonbasic\vcsok\vcsok_hr_task", "data", "employee.json")
    )
    handler.update_item('161c07f6-aadc-4018-b66e-b2fc417c7ddd', "sanyika", "1998.04.25", "CEO", "valami", "pwd", "phone_num", "desc")
    print(handler.employee_dict)
