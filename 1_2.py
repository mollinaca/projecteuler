#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://projecteuler.net/problem=1
1000未満の自然数で3あるいは5の倍数となっている数の総和を求めよ．
"""
# 3の倍数の和と5の倍数の和から15の倍数の和を引く
# 等差数列の和

def msum(p:int, lim:int):
    m = (lim-1)//p
    return p*m*(m+1)//2

n = int(input())
a = 3
b = 5

print (msum(a,n)+msum(b,n)-msum(a*b,n))
