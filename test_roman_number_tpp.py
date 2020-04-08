import unittest

def convert_to_roman(number):
    power_of_hundred = (len(str(number)) - 1) // 2
    result = ""
    for power in range(power_of_hundred + 1):
        if len(str(number)) % 2 == 1 and power == 0:
            part_of_number = int(str(number)[0])
            result += compute_power_hundred(part_of_number, power_of_hundred - power)
        else:
            part_of_number = int(str(number)[2 * power:2 * (power + 1)])
            result += compute_power_hundred(part_of_number, power_of_hundred - power)
    return result


def compute_power_hundred(part_of_number, power_of_hundred):
    list_of_units = ['I', 'X', 'C', 'M', 'undefined']
    list_of_fives = ['V', 'L', 'D', 'undefined']
    unit = list_of_units[2 * power_of_hundred]
    five = list_of_fives[2 * power_of_hundred]
    ten = list_of_units[2 * power_of_hundred + 1]
    fifty = list_of_fives[2 * power_of_hundred + 1]
    hundred = list_of_units[2 * power_of_hundred + 2]

    digit = part_of_number % 10

    if part_of_number <= 39:
        result = part_of_number // 10 * ten
        if digit < 4:
            return result + digit * unit
        if digit == 4:
            return result + unit + five
        if digit == 9:
            return result + unit + ten
        if digit >= 5:
            return result + five + (digit - 5) * unit
    if part_of_number < 50:
        result = ten + fifty + convert_to_roman(part_of_number - 40)
        return result
    if part_of_number < 90:
        return fifty + convert_to_roman(part_of_number - 50)
    if part_of_number < 100:
        return ten + hundred + convert_to_roman(part_of_number - 90)
    else:
        return ""


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

    def test_convert_40_to_XL(self):
        self.assertEqual("XL", convert_to_roman(40))

    def test_convert_41_to_XLI(self):
        self.assertEqual("XLI", convert_to_roman(41))

    def test_convert_44_to_XLI(self):
        self.assertEqual("XLIV", convert_to_roman(44))

    def test_convert_50_to_L(self):
        self.assertEqual("L", convert_to_roman(50))

    def test_convert_90_to_XC(self):
        self.assertEqual("XC", convert_to_roman(90))

    def test_convert_92_to_XCII(self):
        self.assertEqual("XCII", convert_to_roman(92))

    def test_convert_100_to_C(self):
        self.assertEqual("C", convert_to_roman(100))

    def test_convert_1987_to_MCMLXXXVII(self):
        self.assertEqual("MCMLXXXVII", convert_to_roman(1987))
