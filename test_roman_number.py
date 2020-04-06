import unittest


def convert_to_roman(number):
    if number < 4:
       return number * "I"
    return "IV"

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
