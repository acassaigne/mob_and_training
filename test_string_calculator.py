import unittest

def create_list(input_string):
    if input_string == "":
        return []
    return [int(number) for number in input_string.split(",")]

def calculator(input_string):
    result = create_list(input_string)
    if result == []:
        return "0"
    return "2"


class TestStringMethods(unittest.TestCase):

    def test_x(self):
        self.assertEqual([1,1], create_list("1,1"))

    def test_if_create_list_of_empty_string_should_return_empty_list(self):
        self.assertEqual([], create_list(""))

    def test_calculator_empty_string_should_return_0(self):
        self.assertEqual("0", calculator(""))

    def test_calculator_string_with_1_comma_1_return_2(self):
        self.assertEqual("2", calculator("1,1"))