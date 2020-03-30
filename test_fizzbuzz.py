import unittest

def is_fizz(number):
    return number % 3 == 0

def is_buzz(number):
    return number % 5 == 0

def is_fizzbuzz(number):
    return is_fizz(number) and is_buzz(number)

def compute_fizz_buzz(number):
    response = str(number)
    if is_fizz(number):
        response = "fizz"
    if is_buzz(number):
        response = "buzz"
    if is_fizzbuzz(number):
        response = "fizzbuzz"
    return response


class TestStringMethods(unittest.TestCase):

    def test_fizz_buzz_of_1_should_return_1(self):
        self.assertEqual("1", compute_fizz_buzz(1))

    def test_fizz_buzz_of_2_should_return_2(self):
        self.assertEqual("2", compute_fizz_buzz(2))

    def test_fizz_buzz_of_3_should_return_fizz(self):
        self.assertEqual("fizz", compute_fizz_buzz(3))

    def test_fizz_buzz_of_5_should_return_buzz(self):
        self.assertEqual("buzz", compute_fizz_buzz(5))

    def test_fizz_buzz_of_15_should_return_fizzbuzz(self):
        self.assertEqual("fizzbuzz", compute_fizz_buzz(15))