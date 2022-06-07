from dataclasses import dataclass
from datetime import datetime
from dateutil import parser


@dataclass
class Employee:
    name: str
    birth_day: datetime
    position: str
    organisation: str
    password: str
    phone_number: str
    description: str = None

    @staticmethod
    def parse_employee(employee_dict):
        for key, value in employee_dict.items():
            if key == "birth_day":
                employee_dict[key] = parser.parse(value)
            else:
                employee_dict[key] = value
        return Employee(**employee_dict)

    def update_fields(self, update_dict):
        for key, value in update_dict.items():
            if value is None and key != "description":
                continue
            if key == "birth_day":
                setattr(self, key, parser.parse(value))
            else:
                setattr(self, key, value)
