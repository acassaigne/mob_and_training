import unittest


class CannotFindPrimeFactors(Exception):
    pass


def prime_factor(number):
    if number == 0:
        raise CannotFindPrimeFactors
    if number == 1:
        return []
    if number % 2 == 0:
        return [2] + prime_factor(number//2)
    return [number]

class TestPrimeFactorsShould(unittest.TestCase):

    def test_raise_error_for_0(self):
        with self.assertRaises(CannotFindPrimeFactors):
            prime_factor(0)

    def test_return_2_for_2(self):
        self.assertEqual([2], prime_factor(2))

    def test_return_3_for_3(self):
        self.assertEqual([3], prime_factor(3))
        
    def test_return_4_for_4(self):
        self.assertEqual([2, 2], prime_factor(4))

    def test_return_5_for_5(self):
        self.assertEqual([5], prime_factor(5))

    def test_return_2_and_3_for_6(self):
        self.assertEqual([2, 3], prime_factor(6))

    def test_return_2_2_2_for_8(self):
        self.assertEqual([2,2,2], prime_factor(8))

