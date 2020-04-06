import unittest

def convert_to_power_of_ten(number):
    numbers_in_char = list(str(number))[::-1]
    return [int(char) for char in numbers_in_char]

def generate_roman_number_for_power_of_ten(digit, power_of_ten):
    start_segment = get_roman_symbol_for_start_segment(power_of_ten)
    half_segment = get_roman_symbol_for_half_segment(power_of_ten)
    next_segment = get_roman_symbol_for_start_segment(power_of_ten + 1)
    if digit == 0:
        result = ''
    if digit < 4:
        result = digit * start_segment
    if digit == 4:
        result = start_segment + half_segment
    if 5 <= digit <= 8:
        result = half_segment + (digit % 5) * start_segment
    if digit == 9:
        result = start_segment + next_segment
    return result

def get_roman_symbol_for_start_segment(power_of_ten):
    dictionary_start_segment = {0: 'I', 1: 'X', 2: 'C', 3 : 'M'}
    return dictionary_start_segment[power_of_ten]

def get_roman_symbol_for_half_segment(power_of_ten):
    dictionary_half_segment = { 0 : 'V', 1 : 'L', 2 : 'D'}
    return dictionary_half_segment[power_of_ten]

def convert_to_roman(number):
    all_digits = convert_to_power_of_ten(number)
    result = ''
    for power_of_ten in range(len(all_digits)):
        digit = all_digits[power_of_ten]
        result += generate_roman_number_for_power_of_ten(digit,power_of_ten)
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
