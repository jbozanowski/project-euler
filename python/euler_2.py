# -*- coding: utf-8 -*-


def euler_2():
    def fib_sum_even_till_max(a, b, sum_even, max_term):
        if b > max_term:
            return sum_even
        if b % 2 == 0:
            sum_even += b
        return fib_sum_even_till_max(b, a+b, sum_even, max_term)

    MAX_TERM = 4000000
    sum_even = 0
    return fib_sum_even_till_max(1, 2, sum_even, MAX_TERM)


if __name__ == '__main__':
    print euler_2()
