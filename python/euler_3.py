# -*- coding: utf-8 -*-

# Problem 3 - Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


from math import sqrt


def euler_3():
    target = 600851475143
    max_factor = 0

    def _check_prime(x):
        limit = int(round(sqrt(x)))
        for i in xrange(2, limit+1):
            if x % i == 0:
                return False
        return True
    
    target_limit = int(round(sqrt(target)))
    for i in xrange(2, target_limit+1):
        if target % i == 0 and _check_prime(i) and i > max_factor:
            max_factor = i
    return max_factor


if __name__ == '__main__':
    assert euler_3() == 6857
