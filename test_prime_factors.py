import unittest
import math

class CannotFindPrimeFactors(Exception):
    pass


def prime_factor(number):
    if number == 0:
        raise CannotFindPrimeFactors
    if number == 1:
        return []
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return [i] + prime_factor(number // i)
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
        self.assertEqual([2, 2, 2], prime_factor(8))

    def test_return_3_3_for_9(self):
        self.assertEqual([3, 3], prime_factor(9))

    def test_return_3_5_for_15(self):
        self.assertEqual([3, 5], prime_factor(15))

    def test_return_3_7_for_21(self):
        self.assertEqual([3, 7], prime_factor(21))

    def test_return_5_7_for_35(self):
        self.assertEqual([5, 7], prime_factor(35))
