# -*- coding: utf-8 -*-

# Problem 7 - 10001st prime

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.

# What is the 10 001st prime number?

from common import is_prime


def euler_7():

    prime_count = 0
    PRIME_COUNT_TARGET = 10001
    LIMIT = 9999999999999 # arbitrary
    for i in xrange(LIMIT):
        if is_prime(i):
            prime_count += 1
            if prime_count == PRIME_COUNT_TARGET:
                return i


if __name__ == '__main__':
    assert euler_7() == 104723
