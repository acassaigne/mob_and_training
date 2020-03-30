import unittest


def compute_fizz_buzz(number):
    return str(number)


class TestStringMethods(unittest.TestCase):

    def test_fizz_buzz_of_1_should_return_1(self):
        self.assertEqual("1", compute_fizz_buzz(1))

    def test_fizz_buzz_of_2_should_return_2(self):
        self.assertEqual("2", compute_fizz_buzz(2))

    def test_fizz_buzz_of_3_should_return_fizz(self):
        self.assertEqual("fizz", compute_fizz_buzz(3))