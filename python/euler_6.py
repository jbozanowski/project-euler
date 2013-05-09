# -*- coding: utf-8 -*-


def euler_6():
    def _square_of_sum(max_int):
        return sum(range(1, max_int+1)) ** 2

    def _sum_of_squares(max_int):
        return sum(map(lambda x: x * x, range(1, max_int+1)))

    m = 100
    return _square_of_sum(m) - _sum_of_squares(m)


if __name__ == '__main__':
    assert euler_6() == 25164150
