import unittest
from datetime import datetime
from employee import Employee

class MyTestCase(unittest.TestCase):
    def test_parsing(self):
        empl = Employee.parse_employee({
            "name": "sanyika",
            "birth_day": "1998.04.25",
            "position": "pos",
            "organisation": "org",
            "password": "pwd",
            "phone_number": "+3630",
            "description": None
        })
        self.assertEqual(empl.name, "sanyika")
        self.assertEqual(str(empl.birth_day), "1998-04-25 00:00:00")
        self.assertEqual(empl.position, "pos")
        self.assertEqual(empl.organisation, "org")
        self.assertEqual(empl.password, "pwd")
        self.assertEqual(empl.phone_number, "+3630")
        self.assertEqual(empl.description, None)

    def test_datetime_conversion(self):
        empl = Employee.parse_employee({
            "name": "sanyika",
            "birth_day": "1998.04.25",
            "position": "pos",
            "organisation": "org",
            "password": "pwd",
            "phone_number": "+3630",
            "description": None
        })
        self.assertEqual(type(empl.birth_day), datetime)


if __name__ == '__main__':
    unittest.main()
