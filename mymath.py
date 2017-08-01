#coding=utf-8

import functools


def memoize(fn):
    known = dict()

    @functools.wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]
    return memoizer


def t(fn):

    @functools.wraps(fn)
    def t1(fn):
        return fn
    return t1


@memoize
def nsum(n):
    """返回前n个数字的和"""
    assert(n >= 0), 'n must be >= 0'

    def _nsum(n):
        if n == 0:
            return 0
        return n + _nsum(n-1)
    return _nsum(n)


@memoize
def fibonacci(n):
    """返回斐波那契数列的第n个数"""
    assert(n >= 0), 'n must be >= 0'

    @memoize
    def _fibonacci(n):
        if n in (0, 1):
            return n
        return _fibonacci(n-1) + _fibonacci(n-2)
    return _fibonacci(n)

if __name__ == '__main__':
    from timeit import Timer
    measure = [{'exec': 'fibonacci(100)', 'import': 'fibonacci', 'func': fibonacci},
               {'exec': 'nsum(200)', 'import': 'nsum', 'func': nsum}]
    for m in measure:
        t = Timer('{}'.format(m['exec']), 'from __main__ import {}'.format(m['import']))
        print('name: {}, doc: {}, executing: {}, time: {}'.format(m['func'].__name__,
                                                                  m['func'].__doc__,
                                                                  m['exec'], t.timeit()))