import json
import os
from datetime import datetime, date
from employee import Employee


class DataHandler:

    def __init__(self, json_path: str):
        self.json_path = json_path
        self.employee_dict = dict()
        self.load_data()

    def load_data(self):
        if not os.path.exists(self.json_path):
            if self.employee_dict is {}:
                self.employee_dict = {"employee_list": []}
        else:
            with open(self.json_path, "r", encoding="utf-8") as fp:
                loaded_data = json.load(fp)
                self.employee_dict["employee_list"] = []
                for element in loaded_data["employee_list"]:
                    self.employee_dict["employee_list"].append(Employee.parse_employee(element))

    @staticmethod
    def json_serial(obj):

        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        else:
            return str(obj)
        raise TypeError("Type %s not serializable" % type(obj))

    def write_data(self):
        with open(self.json_path, "w", encoding="utf-8") as fp:
            temp_inv = {"employee_list": []}
            for element in self.employee_dict["employee_list"]:
                temp_inv["employee_list"].append(vars(element))
            json.dump(temp_inv, fp, indent=4, default=self.json_serial)

    def __get_item(self, name: str) -> (int, Employee):
        for i, item in enumerate(self.employee_dict["employee_list"]):
            if item.name == name.lower():
                return i, item
        else:
            return None, None

    def delete_item(self, name: str) -> str:
        i, _ = self.__get_item(name)
        if i:
            del self.employee_dict["employee_list"][i]
            msg = f"Successfully deleted {name}"
        else:
            raise ValueError(f"No item found with given name {name}")
        self.write_data()
        return msg

    def add_item(
            self, name: str, birth_day: str, position: str,
            organisation: str, password: str, phone_number: str,
            description: str = None) -> str:
        input_values = locals().items()
        i, _ = self.__get_item(name)
        if i:
            raise ValueError("Employee found with given name")
        else:
            msg = f"Adding new employee with {name} name"
            temp_dict = dict()
            for key, value in input_values:
                if key == "self":
                    continue
                temp_dict[key] = value
            employee = Employee.parse_employee(temp_dict)
            self.employee_dict["employee_list"].append(employee)
        self.write_data()
        return msg

    def update_item(
            self, name: str, birth_day: datetime = None, position: str = None,
            organisation: str = None, password: str = None, phone_number: str = None,
            description: str = None) -> str:
        input_values = locals().items()
        i, _ = self.__get_item(name)
        if i:
            msg = f"Updated price for employee with {name} name"
            for key, value in input_values:
                if key == "self":
                    continue
                if value is None and key != "description":
                    continue
                else:
                    self.employee_dict["employee_list"][i][key] = value
        else:
            raise ValueError("Item not found with given name")
        self.write_data()
        return msg


if __name__ == "__main__":
    handler = DataHandler(
        json_path=os.path.join(r"C:\\Users\\vcsok\\Desktop\\pythonbasic\\vcsok_hr_task\\", "data", "employee.json")
    )
    handler.add_item("sa", "1998.04.25", "CEO", "valami", "pwd", "phone_num", "desc")
    print(handler.employee_dict)