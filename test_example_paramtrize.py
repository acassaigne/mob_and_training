from prime_factor import prime_factor
import pytest
import unittest

@pytest.mark.parametrize("number, prime_numbers_expected",
                         [(2, [2]),
                          (3, [3]),
                          (4, [2, 2])
                          ])
def test_prime_numbers(number, prime_numbers_expected):
    assert prime_factor(number) == prime_numbers_expected

