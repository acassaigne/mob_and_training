import unittest


def convert_to_roman(number):
    if number < 4:
       return number * "I"
    if number == 4:
        return "IV"
    if number >= 5 and number <=8:
        return "V" + (number % 5) * "I"
    return 'IX'


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