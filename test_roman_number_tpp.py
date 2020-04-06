import unittest

def convert_to_roman(number):
    digit = number % 10
    result = number // 10 * 'X'
    if digit < 4:
        return result + digit * 'I'
    if digit == 4:
        return result + 'I'+'V'
    if digit == 9:
        return result + 'I' + 'X'
    if digit >= 5:
        return result + 'V' + (digit - 5) * 'I'

class TestRomanNumber(unittest.TestCase):

    def test_convert_0_to_empty_string(self):
        self.assertEqual("", convert_to_roman(0))

    def test_convert_1_to_I(self):
        self.assertEqual("I", convert_to_roman(1))

    def test_convert_4_to_IV(self):
        self.assertEqual("IV", convert_to_roman(4))

    def test_convert_5_to_V(self):
        self.assertEqual("V", convert_to_roman(5))

    def test_convert_6_to_VI(self):
        self.assertEqual("VI", convert_to_roman(6))

    def test_convert_7_to_VII(self):
        self.assertEqual("VII", convert_to_roman(7))

    def test_convert_9_to_IX(self):
        self.assertEqual("IX", convert_to_roman(9))

    def test_convert_7_to_VII(self):
        self.assertEqual("X", convert_to_roman(10))

    def test_convert_39_to_XXXIX(self):
        self.assertEqual("XXXIX", convert_to_roman(39))
