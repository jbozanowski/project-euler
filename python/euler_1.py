# -*- coding: utf-8 -*-


def euler_1():
    check = lambda x: x % 3 == 0 or x % 5 == 0
    return sum([x for x in range(1000) if check(x)])
    

if __name__ == '__main__':
    assert euler_1() == 233168
