#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://projecteuler.net/problem=2
4000000未満の偶数のフィボナッチ数の総和を求めよ．
"""
n = int(input())
total = 0
f0 = 1
f1 = 1

while True:
    f = f0 + f1
    if f >= n:
        exit (0)
    if f%2 == 0:
        total += f
    f0 = f1
    f1 = f