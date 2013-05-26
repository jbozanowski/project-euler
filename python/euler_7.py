# -*- coding: utf-8 -*-

# Problem 7 - 10001st prime

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.

# What is the 10 001st prime number?


from math import sqrt


def euler_7():
    def _is_prime(x):
        limit = int(round(sqrt(x)))
        for i in xrange(2, limit+1):
            if x % i == 0:
                return False
        return True

    prime_count = 0
    PRIME_COUNT_TARGET = 10001
    i = 0
    LIMIT = 9999999999999 # arbitrary
    while i < LIMIT:
        if _is_prime(i):
            #print '%d - a prime!' % (i, )
            prime_count += 1
            if prime_count == PRIME_COUNT_TARGET:
                return i
        i += 1


if __name__ == '__main__':
    assert euler_7() == 104723
