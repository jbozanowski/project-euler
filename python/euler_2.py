# -*- coding: utf-8 -*-


def euler_2():
    MAX_TERM = 4000000
    sum_even = [0]

    def fib_sum_even_till_max(a, b):
        if b > MAX_TERM:
            return None
        if b % 2 == 0:
            sum_even[0] += b
        fib_sum_even_till_max(b, a+b)

    fib_sum_even_till_max(1, 2)
    return sum_even[0]


if __name__ == '__main__':
    print euler_2()
