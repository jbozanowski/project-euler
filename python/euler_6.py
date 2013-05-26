# -*- coding: utf-8 -*-

# Problem 6 - Sum square difference

# The sum of the squares of the first ten natural numbers is,
#
#   1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,
# 
# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 - 385 = 2640.
 
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.


def euler_6():
    def _square_of_sum(max_int):
        return sum(range(1, max_int+1)) ** 2

    def _sum_of_squares(max_int):
        return sum(map(lambda x: x * x, range(1, max_int+1)))

    m = 100
    return _square_of_sum(m) - _sum_of_squares(m)


if __name__ == '__main__':
    assert euler_6() == 25164150
