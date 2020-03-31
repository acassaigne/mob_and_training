import unittest

def _create_list(input_string):
    input_string = input_string.replace("\n",",")
    if input_string == "":
        return []
    return [int(number) for number in input_string.split(",")]

def calculator(input_string):
    result = _create_list(input_string)
    if result == []:
        return "0"
    return str(sum(result))


class TestStringMethods(unittest.TestCase):

    def test_calculator_empty_string_should_return_0(self):
        self.assertEqual("0", calculator(""))

    def test_calculator_string_with_1_comma_1_return_2(self):
        self.assertEqual("2", calculator("1,1"))

    def test_calculator_string_with_1_comma_2_newline_3_return_6(self):
        self.assertEqual("6", calculator("1,2\n3"))

    def test_delimiter_detector_string_semicolon(self):
        self.assertEqual((";","1,2"),delimiter_detector("//;\n1;2"))

