#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @project : nac-ele
# @Author  : Eagle
# @Site    : 
# @File    : test9.py
# @Time    : 2021/7/7 23:34
# @Software: PyCharm
import time
import itertools as it

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
start = time.time()
number =[1,2,3,4,5,6,7,8,9,10]
# print(set(permutations(number, 10)))
print(set(it.permutations(number, 10)))
print(time.time() - start)