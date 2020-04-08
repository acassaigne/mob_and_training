import unittest


class CannotFindPrimeFactors(Exception):
    pass


def prime_factor(number):
    raise CannotFindPrimeFactors

class TestPrimeFactorsShould(unittest.TestCase):

    def test_raise_error_for_zero(self):
        with self.assertRaises(CannotFindPrimeFactors):
            prime_factor(0)

    def test_y(self):
        



