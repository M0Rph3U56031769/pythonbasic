import unittest

from unittest_gyak.main import ToBeTested


class TestStringMethods(unittest.TestCase):

    def setUp(self) -> None:
        print("\nStart the tests...\n you can setup logging, network stack, etc. in setUp()")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        text = 'hello world'
        self.assertEqual(text.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            text.split(2)

    def tearDown(self) -> None:
        print("Ending the tests... You can close network connections and such things Bye!")


class TestIntMethods(unittest.TestCase):

    TBT_Instance = ToBeTested()

    def test_variable(self):
        self.assertEqual(self.TBT_Instance.print_message, 42)

    def test_print_number_pass(self):
        self.assertEqual(self.TBT_Instance.print_number(), 42)

    def test_print_number_fail(self):
        self.assertEqual(self.TBT_Instance.print_number(), 43)


if __name__ == '__main__':
    unittest.main()
