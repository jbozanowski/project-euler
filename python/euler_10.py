# -*- coding: utf-8 -*-

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


from common import is_prime


LIMIT = 2000000

# More concise, but uses non-constant memory.
#def euler_10():
    #return sum([i for i in xrange(2, LIMIT) if is_prime(i)])

def euler_10():
    sum_of_primes = 0
    for i in xrange(2, LIMIT):
        if is_prime(i):
            sum_of_primes += i
    return sum_of_primes


if __name__ == '__main__':
    assert euler_10() == 142913828922
