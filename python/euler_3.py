# -*- coding: utf-8 -*-

# Problem 3 - Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


from math import sqrt

from common import is_prime


def euler_3():
    target = 600851475143
    max_factor = 0
    target_limit = int(round(sqrt(target)))
    for i in xrange(2, target_limit+1):
        if target % i == 0 and is_prime(i) and i > max_factor:
            max_factor = i
    return max_factor


if __name__ == '__main__':
    assert euler_3() == 6857
