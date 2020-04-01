import unittest

def _delimiter_detector(input_string):
    delimiter = ","
    string_numbers = input_string
    if _has_define_delimiter(input_string):
        delimiter = _get_delimiter(input_string)
        string_numbers = _remove_delimiter_definition(input_string)
    return (delimiter, string_numbers)

def _has_define_delimiter(input_string):
    return input_string[0:2] == "//"

def _remove_delimiter_definition(input_string):
    return input_string[4:]

def _get_delimiter(input_string):
    return input_string[2]

def format_float_if_is_int(number):
    number = float(number)
    if int(number) == number:
        return int(number)
    return number

def _create_list(input_string):
    separator, number_string = _delimiter_detector(input_string)
    number_string = number_string.replace("\n", separator)
    if number_string == "":
        return []
    return [format_float_if_is_int(number) for number in number_string.split(separator)]

def calculator(input_string):
    result = _create_list(input_string)
    if any([number < 0 for number in result]):
        negative_number_list = [str(number) for number in result if number < 0]
        raise InvalidNegativeNumberException("Negative numbers: {0}".format(",".join(negative_number_list)))
    if not result:
        return "0"
    return str(sum(result))


class InvalidNegativeNumberException(Exception):
    def __init__(self, message):
        self.message = message


class TestStringMethods(unittest.TestCase):

    def test_calculator_empty_string_should_return_0(self):
        self.assertEqual("0", calculator(""))

    def test_calculator_string_with_1_comma_1_return_2(self):
        self.assertEqual("2", calculator("1,1"))

    def test_calculator_string_with_1_comma_2_newline_3_return_6(self):
        self.assertEqual("6", calculator("1,2\n3"))

    def test_delimiter_detector_string_semicolon(self):
        self.assertEqual((",", "1,2"), _delimiter_detector("1,2"))

    def test_delimiter_detector_string_semicolon_more_complex(self):
        self.assertEqual((';',"1;2"), _delimiter_detector("//;\n1;2"))

    def test_delimiter_detector_string_semicolon_1_2_should_return_3(self):
        self.assertEqual("3", calculator("//;\n1;2"))

    def test_calculator_negative_number_should_raise_exception(self):
        with self.assertRaises(InvalidNegativeNumberException):
            calculator("-1")

    def test_calculator_negative_input_should_return_negative_numbers(self):
        try:
            calculator("-1.1,2")
        except InvalidNegativeNumberException as e:
            self.assertEqual(e.message, "Negative numbers: -1.1")

