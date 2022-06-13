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

    def __str__(self):
        return \
            f"""Name: {self.name}
        Birth Day: {str(self.birth_day)}
        Position: {self.position}
        Organisation: {self.organisation}
        Password: {self.password}
        Phone Number: {self.phone_number}
        Description: {self.description}"""

    @staticmethod
    def parse_employee(employee_dict):
        """
        Creates employee instance from dictionary
            Parameters:
                employee_dict (dict): dictionary with employee parameters
            Returns:
                (Employee): Employee instance
        """
        for key, value in employee_dict.items():
            if key == "birth_day":
                employee_dict[key] = parser.parse(value)
            else:
                employee_dict[key] = value
        return Employee(**employee_dict)

    def update_fields(self, update_dict) -> None:
        """
        Updates current employee instance from dictionary
            Parameters:
                update_dict (dict): dictionary with employee parameters
            Returns:
                None
        """
        for key, value in update_dict.items():
            if value is "" and key != "description":
                continue
            if key == "birth_day":
                setattr(self, key, parser.parse(value))
            else:
                setattr(self, key, value)
