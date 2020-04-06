import unittest

def convert_to_power_of_ten(number):
    numbers_in_char = list(str(number))[::-1]
    return [int(char) for char in numbers_in_char]

def generate_roman_number_for_power_of_ten(number, start_segment, half_segment, next_segment)

def convert_to_roman(number):
    dictionary_start_segment = { 1 : 'I', 2 : 'X', 3 : 'C'}
    dictionary_half_segment = { 1 : 'V', 2 : 'L', 3 : 'D'}
    all_digits = convert_to_power_of_ten(number)
    result = ''
    for i in range(len(all_digits)):
        start_segment = dictionary_start_segment[i+1]
        half_segment = dictionary_half_segment[i+1]
        next_segment = dictionary_start_segment[i+2]
        number = all_digits[i]
        if number == 0:
            result += ''
        if number < 4:
           result += number * start_segment
        if number == 4:
            result += start_segment + half_segment
        if 5 <= number <= 8:
            result += half_segment + (number % 5) * start_segment
        if number == 9:
            result += start_segment + next_segment
    return result


class TestRomanNumber(unittest.TestCase):

    def test_convert_1_to_I(self):
        self.assertEqual("I", convert_to_roman(1))

    def test_convert_2_to_II(self):
        self.assertEqual("II", convert_to_roman(2))

    def test_convert_3_to_III(self):
        self.assertEqual("III", convert_to_roman(3))

    def test_convert_4_to_IV(self):
        self.assertEqual("IV", convert_to_roman(4))

    def test_convert_5_to_V(self):
        self.assertEqual("V", convert_to_roman(5))

    def test_convert_6_to_VI(self):
        self.assertEqual("VI", convert_to_roman(6))

    def test_convert_9_to_IX(self):
        self.assertEqual("IX", convert_to_roman(9))

    def test_convert_10_to_X(self):
        self.assertEqual("X", convert_to_roman(10))
