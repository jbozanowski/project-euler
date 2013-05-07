# -*- coding: utf-8 -*-


def euler_5():
    HIGHEST_DIVISOR = 20
    START = HIGHEST_DIVISOR
    STOP = 99999999999999 # arbitrary
    divisors = range(HIGHEST_DIVISOR-1, 1, -1)

    def _is_evenly_divisible(x):
        for i in divisors:
            if x % i != 0:
                return False
        return True
        
    i = START
    while i < STOP:
        if _is_evenly_divisible(i):
            return i
        i += HIGHEST_DIVISOR


if __name__ == '__main__':
    assert euler_5() == 232792560
