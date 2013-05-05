# -*- coding: utf-8 -*-

from itertools import combinations


def euler_4():
    def _is_palindromic(integer):
        s = str(integer)
        return all([s[i] == s[(i * -1) - 1] for i in xrange(len(s) / 2)]) 

    palindromes = filter(_is_palindromic,
                         [x[0] * x[1] for x in
                            combinations(xrange(100, 1000), 2)])
    return max(palindromes)


if __name__ == '__main__':
    print euler_4()
