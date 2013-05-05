# -*- coding: utf-8 -*-


def euler_5():
    DIVISORS_END = 20
    START = DIVISORS_END ** 2
    STOP = 99999999999999 # arbitrary
    divisors = range(1, DIVISORS_END+1)

    def _is_evenly_divisible(x):
        for i in divisors:
            if x % i != 0:
                return False
        return True
        
    i = START
    while i < STOP:
        if _is_evenly_divisible(i):
            return i
        i += 1

if __name__ == '__main__':
    print euler_5()
