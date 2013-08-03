# -*- coding: utf-8 -*-

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#   a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product a * b * c.


from itertools import combinations


def _get_pythagorean_triplets(limit):
    for item in combinations(xrange(limit), 3):
        if (item[0] < item[1] < item[2] and
                item[0] ** 2 + item[1] ** 2 == item[2] ** 2):
            yield item


def euler_9():
    # FIXME Extremely inefficient, there has to be a better way...
    for triplet in _get_pythagorean_triplets(1000):
        if triplet[0] + triplet[1] + triplet[2] == 1000:
            return triplet[0] * triplet[1] * triplet[2]


if __name__ == '__main__':
    assert euler_9() == 31875000
