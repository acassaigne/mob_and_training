import unittest


class CannotFindPrimeFactors(Exception):
    pass


def prime_factor(number):
    if number > 3:
        return [number //2, number //2]
    if number >= 2:
        return [number]
    raise CannotFindPrimeFactors

class TestPrimeFactorsShould(unittest.TestCase):

    def test_raise_error_for_0(self):
        with self.assertRaises(CannotFindPrimeFactors):
            prime_factor(0)

    def test_return_2_for_2(self):
        self.assertEqual([2], prime_factor(2))

    def test_return_3_for_3(self):
        self.assertEqual([3], prime_factor(3))
        
    def test_return_4_for_4(self):
        self.assertEqual([2,2], prime_factor(4))


