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