#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://projecteuler.net/problem=1
1000未満の自然数で3あるいは5の倍数となっている数の総和を求めよ．
"""
total=0
for i in range(1000):
    if (i%3 == 0) or (i%5 == 0):
        print (i)
        total += i
print (total)
