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

def format_string_into_float_or_int(string_number):
    float_number = float(string_number)
    int_number = int(float_number)
    if int_number == float_number:
        return int_number
    return float_number

def _create_list(input_string):
    separator, number_string = _delimiter_detector(input_string)
    number_string = number_string.replace("\n", separator)
    if number_string == "":
        return []
    return [format_string_into_float_or_int(number) for number in number_string.split(separator)]

def calculator(input_string):
    result = _create_list(input_string)
    negative_numbers = _extract_negative_numbers(result)
    _raise_error_when_has_negative_numbers(negative_numbers)
    if not result:
        return "0"
    return str(sum(result))

def _raise_error_when_has_negative_numbers(negative_numbers):
    if negative_numbers:
        message = _generate_complementary_error_message_list(negative_numbers)
        raise InvalidNegativeNumberException("Negative numbers: {0}".format(message))

def _generate_complementary_error_message_list(negative_numbers):
    negative_number_list = [str(number) for number in negative_numbers]
    return ",".join(negative_number_list)

def _extract_negative_numbers(numbers):
    return [number for number in numbers if number < 0]

def _has_a_negative_number(number_list):
    return any([number < 0 for number in number_list])

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

