# -*- coding: utf-8 -*-


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
    print euler_3()
