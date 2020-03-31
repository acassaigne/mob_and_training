import unittest

def is_fizz(number):
    return number % 3 == 0

def is_buzz(number):
    return number % 5 == 0

def is_fizzbuzz(number):
    return is_fizz(number) and is_buzz(number)

def compute_fizz_buzz(number):
    response = str(number)
    FIZZ = "fizz"
    BUZZ = "buzz"
    if is_fizz(number):
        response = FIZZ
    if is_buzz(number):
        response = BUZZ
    if is_fizzbuzz(number):
        response = FIZZ + BUZZ
    return response

def sequence_fizzbuzz(max):
    return [compute_fizz_buzz(number) for number in range(1, max+1)]

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

    def test_sequence_fizzbuzz_100_should_return_a_length_list_of_100(self):
        self.assertEqual(100, len(sequence_fizzbuzz(100)))

    def test_sequence_fizzbuzz_first_5_elements_of_list_should_include_one_fizz_and_one_buzz(self):
        self.assertEqual(["1", "2", "fizz", "4", "buzz"], sequence_fizzbuzz(5))

    def test_sequence_fizzbuzz_last_element_of_100_should_be_buzz(self):
        self.assertEqual("buzz", sequence_fizzbuzz(100)[-1])
