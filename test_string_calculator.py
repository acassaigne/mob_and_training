import unittest

def _delimiter_detector(input_string):
    separator = ","
    string_numbers = input_string
    if input_string[0:1] == "//":
        separator = input_string[2]
        string_numbers = input_string[5:]
    return (separator, string_numbers)


def _create_list(input_string):
    separator, number_string = _delimiter_detector(input_string)
    number_string = number_string.replace("\n",separator)
    if number_string == "":
        return []
    return [int(number) for number in number_string.split(separator)]

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
        self.assertEqual((",", "1,2"), _delimiter_detector("1,2"))

    def test_calculator_string_semicolon_1_2_should_return_3(self):
        self.assertEqual("3", calculator("//;\n1;2"))
