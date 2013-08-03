# -*- coding: utf-8 -*-

from math import sqrt


def is_prime(x):
    limit = int(round(sqrt(x)))
    for i in xrange(2, limit+1):
        if x % i == 0:
            return False
    return True
